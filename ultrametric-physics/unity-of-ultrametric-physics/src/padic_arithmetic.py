"""
=============================================================================
Unity of Ultrametric Physics — p-Adic Arithmetic Module
=============================================================================

This module implements fundamental p-adic number operations, including
p-adic absolute value, expansion digit manipulation, and addition.

A p-adic number x = p^v * (a_0 + a_1 p + a_2 p^2 + ...) is represented by
its valuation v and a list of digits a_0, a_1, ...

Usage:
    >>> from padic_arithmetic import PadicNumber
    >>> x = PadicNumber([1, 2], valuation=0, p=5)
    >>> print(x)
    ...21_5 (v=0)
    >>> print(x.abs_p())
    1.0
    >>> y = PadicNumber([3], valuation=0, p=5)
    >>> z = x + y
    >>> print(z)
    ...4_5 (v=0)
"""

import math
from typing import List


class PadicNumber:
    """
    A p-adic number represented by its expansion digits and valuation.

    The p-adic expansion of x is:
        x = p^v * (d_0 + d_1*p + d_2*p^2 + ...)

    where v = v_p(x) is the p-adic valuation, d_i ∈ {0, 1, ..., p-1} are the
    digits, and d_0 ≠ 0 for non-zero x.

    Attributes:
        digits (List[int]): The expansion digits d_0, d_1, ..., d_{N-1}.
        valuation (int): The p-adic valuation v (may be float('inf') for zero).
        p (int): The prime.
    """

    def __init__(self, digits: List[int], valuation: int, p: int):
        """
        Initialize a p-adic number.

        Args:
            digits: List of digits d_0, d_1, ..., each in [0, p-1].
            valuation: p-adic valuation v_p(x). Use float('inf') for zero.
            p: The prime.

        Raises:
            AssertionError: If any digit is outside [0, p-1].
        """
        self.digits = digits
        self.valuation = valuation
        self.p = p
        self._validate()

    def _validate(self):
        """Verify that all digits are valid."""
        for d in self.digits:
            assert 0 <= d < self.p, f"Digit {d} not in [0, {self.p - 1}]"

    def abs_p(self) -> float:
        """
        Compute the p-adic absolute value |x|_p = p^{-v}.

        Returns:
            float: The p-adic absolute value. 0.0 if the number is zero.
        """
        if self.valuation == float('inf'):
            return 0.0
        return float(self.p ** (-self.valuation))

    def __repr__(self) -> str:
        """String representation showing digits and valuation."""
        if self.valuation == float('inf') or all(d == 0 for d in self.digits):
            return "0"
        # Digits displayed in reverse order (standard p-adic notation)
        dig_str = "".join(str(d) for d in self.digits[::-1])
        return f"...{dig_str}_{self.p} (v={self.valuation})"

    def __add__(self, other: 'PadicNumber') -> 'PadicNumber':
        """
        Add two p-adic numbers digit by digit with carry.

        Args:
            other: Another PadicNumber (must have the same prime p).

        Returns:
            PadicNumber: The sum.

        Raises:
            AssertionError: If the primes differ.
        """
        assert self.p == other.p, f"Cannot add p-adic numbers with different primes: {self.p} vs {other.p}"

        v_min = min(self.valuation, other.valuation)
        max_len = max(len(self.digits), len(other.digits))

        carry = 0
        result_digits = []

        for i in range(max_len + 2):  # +2 for possible carry propagation
            d1 = self._get_digit(i)
            d2 = other._get_digit(i)
            s = d1 + d2 + carry
            result_digits.append(s % self.p)
            carry = s // self.p

        # Determine the valuation of the result by trimming leading zeros
        new_v = v_min
        while result_digits and result_digits[0] == 0:
            result_digits.pop(0)
            new_v += 1

        if not result_digits:
            return PadicNumber([0], float('inf'), self.p)

        return PadicNumber(result_digits, new_v, self.p)

    def _get_digit(self, idx: int) -> int:
        """
        Get the digit at a given relative position.

        The absolute position in the expansion is idx + valuation.
        Digits beyond the stored list are treated as 0.

        Args:
            idx: Relative position index (0 = first digit after valuation).

        Returns:
            int: The digit (0 if out of bounds).
        """
        actual_idx = idx + self.valuation
        if actual_idx < 0:
            return 0
        if actual_idx < len(self.digits):
            return self.digits[actual_idx]
        return 0

    def __eq__(self, other: 'PadicNumber') -> bool:
        """Check equality of two p-adic numbers."""
        if self.p != other.p:
            return False
        if self.valuation != other.valuation:
            return False
        max_len = max(len(self.digits), len(other.digits))
        for i in range(max_len):
            if self._get_digit(i) != other._get_digit(i):
                return False
        return True


# =============================================================================
# Example usage
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("p-Adic Arithmetic Examples")
    print("=" * 60)

    # Example 1: 2-adic numbers
    print("\n--- 2-adic numbers ---")
    a = PadicNumber([0, 0, 1], valuation=0, p=2)   # 0 + 0*2 + 1*4 = 4
    b = PadicNumber([1, 1], valuation=0, p=2)       # 1 + 1*2 = 3
    c = a + b
    print(f"4 (2-adic) + 3 (2-adic) = {c}")
    print(f"|4|_2 = {a.abs_p()}")
    print(f"|3|_2 = {b.abs_p()}")

    # Example 2: 5-adic numbers
    print("\n--- 5-adic numbers ---")
    x = PadicNumber([2, 3, 1], valuation=0, p=5)   # 2 + 3*5 + 1*25 = 42
    y = PadicNumber([4], valuation=0, p=5)          # 4
    z = x + y
    print(f"42 (5-adic) + 4 (5-adic) = {z}")

    # Example 3: Numbers with valuation
    print("\n--- Numbers with valuation ---")
    # 25 in 5-adic: valuation 2, digit 1
    twenty_five = PadicNumber([1], valuation=2, p=5)
    print(f"25 = {twenty_five}")
    print(f"|25|_5 = {twenty_five.abs_p()}")  # Should be 5^{-2} = 0.04

    # Example 4: p-adic absolute value inverts intuition
    print("\n--- p-adic absolute value inverts intuition ---")
    big_number = PadicNumber([1], valuation=0, p=2)       # |1|_2 = 1
    huge_power = PadicNumber([1], valuation=100, p=2)     # |2^100|_2 = 2^{-100}
    print(f"|1|_2 = {big_number.abs_p()}")
    print(f"|2^100|_2 = {huge_power.abs_p()}  (vanishingly small!)")

    print("\nDone.")
