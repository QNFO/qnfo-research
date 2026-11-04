"""
=============================================================================
Unity of Ultrametric Physics — p-Adic Schrödinger Equation Solver
=============================================================================

This module implements the split-operator (Trotter-Suzuki) method for
solving the p-adic Schrödinger equation on a truncated Bruhat-Tits tree:

    iħ ∂_t ψ(x,t) = (-ħ²/2m Δ_p + V(x)) ψ(x,t)

where Δ_p is the Vladimirov Laplacian on a depth-N tree with p^N leaves.

Key features:
- Fast Vladimirov Transform (Walsh-Hadamard for p=2)
- Split-operator time evolution
- Precomputed kinetic energy spectrum
- Support for arbitrary potentials

Usage:
    >>> from padic_schrodinger import PadicSchrodinger
    >>> import numpy as np
    >>> solver = PadicSchrodinger(p=2, depth=8, mass=1.0)
    >>> psi0 = np.ones(solver.n_leaves) / np.sqrt(solver.n_leaves)
    >>> V = np.zeros(solver.n_leaves)
    >>> history = solver.evolve(psi0, V, t_max=10.0, dt=0.1)
"""

import numpy as np
import math
from typing import Callable, List, Tuple, Optional


class PadicSchrodinger:
    """
    Split-operator solver for the p-adic Schrödinger equation on a
    truncated Bruhat-Tits tree.

    The tree has depth `depth`, branching factor `p`, and `p^depth` leaves.
    The state vector ψ[i] gives the wavefunction amplitude at leaf i.

    Attributes:
        p (int): Branching factor (prime).
        depth (int): Tree depth.
        n_leaves (int): Total number of leaves = p^depth.
        mass (float): Particle mass.
        hbar (float): Reduced Planck constant.
        kinetic_spectrum (np.ndarray): Precomputed kinetic energies |k|_p²/(2m).
    """

    def __init__(self, p: int, depth: int, mass: float, hbar: float = 1.0):
        """
        Initialize the p-adic Schrödinger solver.

        Args:
            p: Branching factor (prime, typically 2, 3, or 5).
            depth: Tree depth. Number of leaves = p^depth.
            mass: Particle mass in natural units.
            hbar: Reduced Planck constant (default 1.0).
        """
        self.p = p
        self.depth = depth
        self.n_leaves = p ** depth
        self.mass = mass
        self.hbar = hbar
        self._precompute_kinetic()

    def _precompute_kinetic(self):
        """
        Precompute the kinetic energy spectrum.

        The kinetic energy in momentum space is:
            E_kin(k) = ħ² |k|_p² / (2m)

        where |k|_p = p^{-v_p(k)} for k ≠ 0, and 0 for k = 0.
        """
        self.kinetic_spectrum = np.zeros(self.n_leaves)

        for i in range(self.n_leaves):
            v = self._valuation(i)
            if v == float('inf'):
                k_abs = 0.0
            else:
                k_abs = self.p ** (-v)
            self.kinetic_spectrum[i] = (self.hbar ** 2) * (k_abs ** 2) / (2 * self.mass)

    def _valuation(self, n: int) -> float:
        """
        Compute the p-adic valuation v_p(n) for an integer n.

        The valuation is the exponent of p in the prime factorization of n.
        For n = 0, returns infinity.

        Args:
            n: A non-negative integer.

        Returns:
            The valuation, or float('inf') for n = 0.
        """
        if n == 0:
            return float('inf')
        v = 0
        while n % self.p == 0:
            n //= self.p
            v += 1
        return v

    def _frac_part(self, x: int) -> float:
        """
        Compute the p-adic fractional part of an integer.

        For p-adic Fourier transform, we need exp(2πi {k·x}_p) where
        {·}_p extracts the fractional part (negative powers of p).

        Args:
            x: Integer (product of momentum and position indices).

        Returns:
            float: The fractional part as a real number in [0, 1).
        """
        result = 0.0
        power = self.p
        for _ in range(self.depth):
            digit = (x // int(power)) % self.p
            result += digit / power
            power *= self.p
        return result

    def padic_fourier(self, psi: np.ndarray) -> np.ndarray:
        """
        Compute the p-adic Fourier transform.

        For p=2, uses the fast Walsh-Hadamard transform (O(N log N)).
        For general p, constructs the full character matrix (O(N²)).

        Args:
            psi: Wavefunction in position basis (length p^depth).

        Returns:
            Wavefunction in momentum basis.
        """
        if self.p == 2:
            # Fast Walsh-Hadamard transform
            n = len(psi)
            psi_k = psi.copy().astype(complex)
            step = 1
            while step < n:
                for i in range(0, n, 2 * step):
                    for j in range(step):
                        u = psi_k[i + j]
                        v = psi_k[i + j + step]
                        psi_k[i + j] = (u + v) / np.sqrt(2)
                        psi_k[i + j + step] = (u - v) / np.sqrt(2)
                step *= 2
            return psi_k
        else:
            # General p: full character matrix
            n = len(psi)
            chi = np.zeros((n, n), dtype=complex)
            for i in range(n):
                for j in range(n):
                    chi[i, j] = np.exp(2j * np.pi * self._frac_part(i * j))
            return chi @ psi

    def inverse_padic_fourier(self, psi_k: np.ndarray) -> np.ndarray:
        """
        Compute the inverse p-adic Fourier transform.

        For p=2, the Walsh-Hadamard transform is self-inverse (up to normalization).
        For general p, uses the conjugate character matrix divided by n.

        Args:
            psi_k: Wavefunction in momentum basis.

        Returns:
            Wavefunction in position basis.
        """
        if self.p == 2:
            return self.padic_fourier(psi_k)  # Self-inverse for normalized WH
        else:
            n = len(psi_k)
            chi_conj = np.zeros((n, n), dtype=complex)
            for i in range(n):
                for j in range(n):
                    chi_conj[i, j] = np.exp(-2j * np.pi * self._frac_part(i * j))
            return chi_conj @ psi_k / n

    def evolve_step(self, psi: np.ndarray, V: np.ndarray, dt: float) -> np.ndarray:
        """
        Perform one time step using split-operator (Trotter-Suzuki) method.

        The evolution operator is approximated as:
            U(dt) ≈ exp(-i V dt/(2ħ)) · exp(-i T dt/ħ) · exp(-i V dt/(2ħ))

        where T is the kinetic operator (diagonal in momentum basis) and
        V is the potential (diagonal in position basis).

        Args:
            psi: Current wavefunction.
            V: Potential array (length = n_leaves).
            dt: Time step.

        Returns:
            Evolved wavefunction after one step.
        """
        # Half-step in position space (potential)
        psi = psi * np.exp(-0.5j * V * dt / self.hbar)

        # Full step in momentum space (kinetic)
        psi_k = self.padic_fourier(psi)
        psi_k = psi_k * np.exp(-1.0j * self.kinetic_spectrum * dt / self.hbar)

        # Transform back to position space
        psi = self.inverse_padic_fourier(psi_k)

        # Half-step in position space (potential)
        psi = psi * np.exp(-0.5j * V * dt / self.hbar)

        return psi

    def evolve(self, psi0: np.ndarray, V: np.ndarray,
               t_max: float, dt: float,
               callback: Optional[Callable[[float, np.ndarray], None]] = None
               ) -> List[Tuple[float, np.ndarray]]:
        """
        Evolve the wavefunction for a total time t_max.

        Args:
            psi0: Initial wavefunction (must be normalized).
            V: Potential array (length = n_leaves).
            t_max: Total evolution time.
            dt: Time step size.
            callback: Optional function called after each step as callback(t, psi).

        Returns:
            List of (time, wavefunction) tuples at sampled time points.
        """
        n_steps = int(t_max / dt)
        psi = psi0.copy().astype(complex)
        history = [(0.0, psi.copy())]

        for step in range(n_steps):
            psi = self.evolve_step(psi, V, dt)
            t = (step + 1) * dt

            if callback is not None:
                callback(t, psi)

            # Sample periodically for history
            if step % max(1, n_steps // 100) == 0:
                history.append((t, psi.copy()))

        # Ensure final state is recorded
        history.append((t_max, psi.copy()))
        return history


# =============================================================================
# Example: p-adic Harmonic Oscillator
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("p-Adic Schrödinger Solver — Harmonic Oscillator Example")
    print("=" * 60)

    # Parameters
    p = 2
    depth = 6  # 2^6 = 64 leaves
    mass = 1.0
    omega = 1.0
    hbar = 1.0

    solver = PadicSchrodinger(p=p, depth=depth, mass=mass, hbar=hbar)
    n = solver.n_leaves

    # Build harmonic oscillator potential: V(x) = ½ m ω² |x|_p²
    V = np.zeros(n)
    for i in range(n):
        v = solver._valuation(i)
        x_abs = p ** (-v) if v != float('inf') else 0.0
        V[i] = 0.5 * mass * omega**2 * x_abs**2

    # Initial state: Gaussian-like, localized near zero
    psi0 = np.zeros(n, dtype=complex)
    scale = p ** (-3)  # Localization scale
    for i in range(n):
        v = solver._valuation(i)
        x_abs = p ** (-v) if v != float('inf') else 0.0
        psi0[i] = np.exp(-x_abs**2 / (2 * scale**2))
    psi0 /= np.sqrt(np.sum(np.abs(psi0)**2))

    # Evolve and measure
    print(f"Tree: p={p}, depth={depth}, leaves={n}")
    print(f"Evolving for t_max=30.0 with dt=0.1...")

    history = solver.evolve(psi0, V, t_max=30.0, dt=0.1)

    # Compute autocorrelation C(t) = |⟨ψ(0)|ψ(t)⟩|
    times = np.array([t for t, _ in history])
    autocorr = np.array([np.abs(np.vdot(psi0, psi)) for _, psi in history])

    # Spectral analysis via FFT
    from scipy.fft import fft, fftfreq

    n_fft = 2**14
    spectrum = np.abs(fft(autocorr, n=n_fft))
    freqs = fftfreq(n_fft, d=(times[1] - times[0]))
    positive = freqs > 0

    # Find peaks
    peak_freqs = freqs[positive][np.argsort(spectrum[positive])[-5:]]
    peak_amps = spectrum[positive][np.argsort(spectrum[positive])[-5:]]

    print("\nAutocorrelation peaks at frequencies:")
    for f, a in zip(sorted(peak_freqs, reverse=True), sorted(peak_amps, reverse=True)):
        print(f"  f = {f:.3f}  →  |C(f)| = {a:.3f}")

    # Check geometric spacing
    sorted_freqs = sorted(peak_freqs, reverse=True)
    if len(sorted_freqs) >= 2:
        ratio = sorted_freqs[1] / sorted_freqs[2] if len(sorted_freqs) >= 3 else 0
        print(f"\nFrequency ratio (should be ≈ {p}): {ratio:.3f}")
        if abs(ratio - p) < 0.3:
            print("✓ Geometric spacing confirmed!")
        else:
            print("⚠ Geometric spacing not clearly visible (try larger depth)")

    print("\nDone.")
