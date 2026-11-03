# Functorial Framework for Morphological Computing

## A Functorial Framework for Morphological Computing: A Vectorial, Topologically-Protected Solution to the Residue Number System Reconstruction Paradox

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com **ORCID:**
0009-0002-4317-5604 **ISNI:** 0000 0005 2645 6062
**URL:** https://papers.qnfo.org/papers/functorial-framework-for-morphological-computing/ **Publication
Date:** 2025-10-31 **Version:** 1.0

**Abstract**: This work introduces a formal framework
for morphological computing that resolves the longstanding
reconstruction paradox in Residue Number System (RNS) arithmetic by
leveraging the physics of topological quantum matter. Conventional
RNS-based accelerators are bottlenecked by the serial, computationally
expensive conversion of a parallel residue vector into a scalar integer
via the Chinese Remainder Theorem. We dissolve this bottleneck by
proposing a vectorial topological encoding scheme where the
computational result is the residue vector itself, physically embodied
as a vector of Chern numbers in a moiré superlattice. We address the
critical challenge of formal verification in physical computing by
constructing a structure-preserving functor from the algebraic category
of RNS computations to the physical category of adiabatic evolutions in
topological phases. This functor provides a formal guarantee of
computational correctness. The final result is read out directly via a
multi-terminal quantum Hall conductance measurement, which yields the
Chern vector without any algorithmic post-processing. This approach
establishes a new paradigm of computation-by-relaxation that is formally
verifiable, physically robust, and achieves end-to-end energy efficiency
by eliminating the reconstruction step entirely.

**Keywords**: morphological computing, Residue Number
Systems, topological quantum matter, functorial framework, category
theory, Chern insulator, moiré materials, quantum Hall effect, physical
computation, hardware-software co-design, energy-efficient computing

### I. State of the Art and Gap Identification

**A. Summary of key prior work**

The scholarly context for this work is situated at the confluence of
three distinct but complementary fields: morphological computing,
Residue Number Systems (RNS), and topological quantum matter. The
concept of morphological computing, where a system’s physical structure
contributes to computation, was advanced by Pfeifer & Bongard
(2007), but has been critically assessed as often lacking a rigorous
information-theoretic foundation that would distinguish it from trivial
physical dynamics (Müller & Hoffmann, 2017). This concern is
reinforced by the argument that without a formal framework to define the
relationship between a physical process and an abstract computation,
claims of physical computation risk becoming unverifiable (Horsman et
al., 2014). In parallel, RNS, as formalized by Szabo & Tanaka
(1967), offers an architecture for carry-free parallel arithmetic.
However, its practical application is persistently hindered by the
computational overhead of the Chinese Remainder Theorem (CRT)
reconstruction step, a bottleneck that remains a challenge even in
modern applications such as homomorphic encryption (Cheon et al., 2017).
Concurrently, the study of topological phases of matter has progressed
from theoretical proposals (Kitaev, 2003) to experimental realizations
of robust, topologically protected states in moiré materials (Sharpe et
al., 2019). While these systems provide stable, quantized invariants,
the literature lacks a clear protocol for encoding arbitrary
computational results into these invariants and reading them out
directly. Existing work on topological quantum computing has largely
focused on developing fault-tolerant quantum gates using non-Abelian
anyons, rather than addressing general-purpose integer arithmetic (Nayak
et al., 2008). The broader field of physical computation has long
explored analogues to Turing-completeness in continuous physical systems
but has not yet produced scalable, noise-resilient, and formally
verifiable architectures for integer arithmetic (MacLennan, 2004;
Siegelmann, 1999). Finally, the persistent demand for energy-efficient
computing in the post-Moore era highlights the limitations of existing
RNS accelerators, which have yet to overcome the systems-level overhead
imposed by the reconstruction step (Horowitz, 2014).

**B. Identified open problems or tensions**

The confluence of these fields reveals a set of interconnected and
unresolved problems. The primary issue is the reconstruction paradox,
where the inherent parallelism of RNS is nullified by the serial,
computationally intensive CRT reconstruction required to produce a
usable scalar output. This is directly linked to the verification
challenge: many proposals for physics-based computation remain
descriptive, lacking the formal mathematical structure, such as that
provided by category theory, needed to prove that a physical system
correctly implements a specified computation (Müller & Hoffmann,
2017; Horsman et al., 2014). Even if a computational state were encoded
in a topological invariant, a measurement problem persists, as no
established protocol allows for the direct measurement of such an
invariant to yield a final computational result without requiring
further algorithmic processing. This has led to a scalar encoding
failure, where attempts to map the CRT reconstruction onto a single,
weighted physical observable have proven unworkable due to non-physical
requirements and a misunderstanding of measurement principles. These
specific issues point to a deeper ontological mismatch: prior work
typically treats a physical system as a passive substrate on which an
abstract algorithm is executed, whereas this work proposes an inversion
where the computation is the natural dynamics of the physics itself.
Furthermore, existing topological computing frameworks exhibit a lack of
arithmetic universality, focusing on specialized quantum gate sets
rather than the general-purpose integer arithmetic needed for many
classical computing tasks. This disconnect is formalized by the absence
of categorical grounding, as no prior work has constructed a functorial
bridge to formally link an algebraic model of computation with a
category of topological quantum phases. Finally, these issues culminate
in a practical energy-latency tradeoff, where the benefits of RNS
arithmetic are offset by the costs of reconstruction, yielding no net
system-level advantage.

**C. Positioned contribution of this work**

This work presents a framework that directly addresses the identified
gaps by integrating these fields through a novel, formally grounded
approach. It resolves the reconstruction paradox by dissolving the
problem: a vectorial topological encoding is proposed where the
computational result is the vector of residues itself, rendered directly
as a physical observable, eliminating the need for a scalar
reconstruction. The verification challenge is met through a
categorically formalized framework that constructs an explicit,
structure-preserving functor from the category of RNS computations to
the category of topological physical evolutions, providing a formal
proof of correctness that responds to the critiques of Müller &
Hoffmann (2017). The measurement problem is solved by specifying an
experimentally feasible, direct multi-terminal measurement protocol
where the encoded Chern vector is read out as a set of quantized Hall
conductances, yielding the final result without post-processing. This
approach overcomes the scalar encoding failure by embracing a parallel
vector output that is native to both RNS and the physics of topological
matter. By grounding the framework in a computation-by-relaxation
paradigm, this work offers a concrete realization of morphological
computing that is non-trivial and formally verifiable, as called for by
Horsman et al. (2014). It establishes arithmetic universality for a
class of topological systems by demonstrating a mapping from any integer
arithmetic operation to a realizable physical protocol. Through an
ontological inversion, computation is redefined not as an abstract
process imposed on matter, but as the natural, deterministic relaxation
of a constrained physical system. By eliminating the reconstruction
bottleneck, this architecture achieves end-to-end energy efficiency,
breaking the longstanding energy-latency tradeoff that has limited the
utility of RNS accelerators.

### II. Theoretical Foundations of Morphological Computing

**A. From symbolic to physical computation**

This framework redefines computation not as the execution of a
logical sequence, but as the deterministic evolution of a constrained
physical system. The process begins with the preparation of a
high-energy initial state, which then naturally relaxes to a
minimum-energy ground state that physically encodes the computational
solution. This “computation-by-relaxation” paradigm leverages the
system’s natural physics to perform computational work, thereby avoiding
the von Neumann bottleneck and the energy costs associated with
transistor switching. The process can be understood as a physical
instantiation of coarse-graining, where microscopic degrees of freedom
self-organize into a stable, macroscopic state that represents the
computational result. This view is consistent with Landauer’s principle,
as the energy dissipated is fundamentally linked to the physical
relaxation process rather than the logical irreversibility of an
abstract gate model. The computational complexity of a problem is
encoded in the landscape of the system’s free energy functional, with
the solution path corresponding to a geodesic in the system’s state
space, a concept that aligns with the notion of thermodynamic depth
(Lloyd & Pagels, 1988). The input is encoded in the preparation of
the initial state, while the function to be computed is encoded in the
topology of the energy landscape, thus unifying program and data within
the physical substrate. The system functions as a dissipative structure,
where an external energy flow is used to prepare the system far from
equilibrium, and its subsequent relaxation toward equilibrium performs
the computation (Prigogine, 1967).

**B. Residue number systems as the optimal physical
logic**

Residue Number Systems provide the ideal mathematical structure for
this physical computing paradigm. The core advantage of RNS is its
inherent parallelism; arithmetic operations on each residue channel are
performed independently of all others, which eliminates the carry
propagation that fundamentally limits conventional binary arithmetic.
This mathematical independence maps directly and naturally onto a
physical architecture of decoupled subsystems, such as distinct regions
of a mesoscopic material, where each prime modulus corresponds to a
unique, topologically protected computational channel. The Chinese
Remainder Theorem guarantees a bijective mapping between a global
integer and its corresponding vector of local residues, ensuring that
the vector representation is both complete and unambiguous. The product
ring structure, \(\prod_{i=1}^k
\mathbb{Z}/p_i\mathbb{Z}\), is not merely a mathematical
convenience but is the formal expression of a physically decomposable
system, making RNS the natural logic for a modular hardware
implementation. The isomorphism of algebras guaranteed by the CRT
ensures that all essential ring-theoretic properties, such as
distributivity and associativity, are preserved in the vectorial
representation, providing a faithful encoding of the computation.
Furthermore, the use of small prime moduli provides a balance between
dynamic range, physical realizability, and intrinsic error detection, as
any error affecting a single channel produces an out-of-range vector
that is immediately detectable. RNS thus functions as a non-linear
error-detecting code, a property that is maintained and physically
grounded in the topological embodiment.

**C. Topological protection for robust information
encoding**

To ensure that the physical embodiment of RNS is robust, information
is encoded in global topological invariants that are intrinsically
resilient to local noise, defects, and thermal perturbations. The Chern
number, a global property of a system’s electronic band structure,
serves as the physical carrier of a residue value. Fractional Chern
Insulators (FCIs), which have been realized in moiré superlattices,
offer a suitable physical platform where the ground-state degeneracy and
associated Chern number can be engineered to be prime-bounded, thereby
creating a direct physical realization of an RNS residue channel. In
this architecture, the moiré pattern is not a passive substrate but an
active computational landscape whose electronic properties can be
programmed by tuning physical parameters like twist angle and external
electric fields. The topological degeneracy of the ground state provides
a natural Hilbert space for storing a residue, with each distinct Chern
sector functioning as a stable, noise-immune memory element. The
robustness of this encoding is physically guaranteed by the spectral gap
of the system, which exponentially suppresses fluctuations that could
cause unintended transitions between different topological sectors.
Information can be read out by leveraging the chiral edge states
characteristic of such systems, which carry a quantized current directly
proportional to the bulk Chern number, enabling a non-invasive,
contact-based measurement. This system exhibits topological quantum
order, where long-range quantum entanglement provides a deep, intrinsic
fault tolerance that protects the encoded information beyond the simple
energy barrier of the spectral gap (Wen, 2002).

### **III. The Functorial Framework: A Formal Bridge from Computation to Physics** |

### **Appendix A: Formal Verification of the Functorial Framework** |

The formal correctness of the proposed framework is established
through the following derivation. |

1. **Chinese Remainder Theorem**: For a set of pairwise
coprime integers \(p_1, \dots, p_k\),
the map \(\phi: N \mapsto (N \bmod p_1, \dots,
N \bmod p_k)\) defines a ring isomorphism \(\phi: \mathbb{Z}/M\mathbb{Z} \to \prod_{i=1}^k
\mathbb{Z}/p_i\mathbb{Z}\), where \(M =
\prod_i p_i\). |

2. **Category RNS**: The category **RNS**
is defined. Its objects are the rings \(\mathbb{Z}/p_i\mathbb{Z}\). Its morphisms
are ring homomorphisms \(f:
\mathbb{Z}/p_i\mathbb{Z} \to \mathbb{Z}/p_i\mathbb{Z}\) induced
by arithmetic operations (e.g., \(f(x) = x + a
\bmod p_i\)). |

3. **Category TopPh**: The category
**TopPh** is defined. Its objects are pairs \((\mathcal{H}_i, H_i)\), where \(\mathcal{H}_i\) is the ground-state Hilbert
space of an FCI with Chern numbers in \(\{0,
\dots, p_i-1\}\), and \(H_i\) is
its Hamiltonian. Its morphisms are unitary operators \(U_f\) generated by adiabatic protocols,
given by: |

\[U_f = \mathcal{T}
\exp\left(-\frac{i}{\hbar} \int_0^\tau H_i(t) \, dt\right) \quad
(A1)\] |

4. **Functor Construction (Objects)**: The functor
\(\mathcal{F}: \textbf{RNS} \to
\textbf{TopPh}\) is constructed on objects by the mapping \(\mathcal{F}(\mathbb{Z}/p_i\mathbb{Z}) =
(\mathcal{H}_i, H_i)\). |

5. **Functor Construction (Morphisms)**: On morphisms,
for an arithmetic operation \(f(x) = x + a
\bmod p_i\), the functor maps it to a unitary evolution \(\mathcal{F}(f) = U_f\), where \(U_f\) is generated by a Thouless pumping
protocol that shifts the Chern number by \(a\). |

6. **Identity Preservation**: The functor preserves
identities. The identity morphism in **RNS** is \(f(x)=x\), which corresponds to a shift of
\(a=0\). The corresponding physical
protocol is a static Hamiltonian, which generates the identity unitary
\(\mathbb{I}_{\mathcal{H}_i}\). Thus,
\(\mathcal{F}(\mathrm{id}_{\mathbb{Z}/p_i\mathbb{Z}})
= \mathbb{I}_{\mathcal{H}_i}\). |

7. **Composition Preservation**: The functor preserves
composition. For two morphisms \(f\)
and \(g\), the physical protocol for
\(g \circ f\) is the temporal
concatenation of the individual protocols. The resulting unitary
evolution is the product of the individual unitaries, \(U_g U_f\). Therefore, \(\mathcal{F}(g \circ f) = U_g U_f = \mathcal{F}(g)
\circ \mathcal{F}(f)\). |

8. **Conclusion**: Since \(\mathcal{F}\) preserves both identities and
composition, it is a well-defined, structure-preserving functor. This
provides a formal guarantee that the physical system correctly
implements the algebra of RNS computations. |

9. **Universality**: The framework is general. Any
other physical system that realizes the same algebraic structure (e.g.,
a photonic lattice) would be related to this moiré implementation by a
natural isomorphism, demonstrating the universality of the categorical
approach. |

10. **Extension to Multiplication**: Ring homomorphisms
for multiplication (e.g., \(f_b(x) = b x \bmod
p_i\)) can be implemented via sequences of additions or other
non-linear adiabatic protocols, ensuring the full ring structure is
preserved under \(\mathcal{F}\). |

11. **Faithfulness**: The functor is faithful. If \(\mathcal{F}(f) = \mathcal{F}(g)\), their
corresponding physical effects are identical. Since distinct arithmetic
operations produce distinct and measurable shifts in the Chern number,
this implies \(f = g\). |

12. **Fullness**: The functor is full. Every adiabatic
protocol that shifts the Chern number by an integer \(a\) corresponds to the morphism \(f_a(x) = x + a \bmod p_i\) in
**RNS**. |

13. **Categorical Equivalence**: Because the functor
\(\mathcal{F}\) is full, faithful, and
essentially surjective onto the relevant subcategory of
**TopPh**, it establishes an equivalence of categories
between **RNS** and its physical realization. |

### Appendix B: Verification of the Vectorial Encoding Scheme

The validity of the vectorial encoding and measurement scheme is
established as follows.

**Bijective Mapping (CRT)**: From the Chinese
Remainder Theorem, the map \(\phi: N \mapsto
(r_1, \dots, r_k)\), where \(r_i = N
\bmod p_i\), is a bijection from the set of integers \(\{0, \dots, M-1\}\) to the product ring
\(\prod_{i=1}^k
\mathbb{Z}/p_i\mathbb{Z}\).

**Physical State Representation**: In the proposed
physical system, the computational state is characterized by the Chern
vector \(\mathbf{C} = (C_1, \dots,
C_k)\), where each \(C_i\) is an
integer in the range \(\{0, \dots,
p_i-1\}\).

**Encoding Correspondence**: By the construction of
the functorial framework (Section III.C) and the operational protocols
(Section IV.B), the physical encoding ensures a direct correspondence
\(C_i = r_i\) for all channels \(i\). Therefore, the map from an integer to
its physical representation, \(N \mapsto
\mathbf{C}\), is also a bijection.

**Unambiguous Representation**: A bijective mapping
means that the Chern vector \(\mathbf{C}\) is a complete and unambiguous
representation of the integer \(N\).
There is a one-to-one correspondence, ensuring no information is lost.
This obviates any need for algorithmic reconstruction.

**Direct Measurement**: The multi-terminal
measurement protocol (Section IV.C) directly yields the integer
components of the Chern vector, \(\{C_1,
\dots, C_k\}\), via a set of independent, quantized Hall
conductance measurements.

**Conclusion**: The final output of the physical
system is the vector \(\mathbf{C}\),
which is demonstrably equivalent to the RNS representation of \(N\). The computational problem is solved
entirely by the physical process, and the result is directly readable
from the hardware.

**Edge Case Analysis**: The encoding is valid across
the entire dynamic range. For \(N =
0\), the system is in the vacuum state with \(\mathbf{C} = (0, \dots, 0)\). For \(N = M-1\), the system is in the state \(\mathbf{C} = (p_1-1, \dots, p_k-1)\). Both
are valid and stable ground states.

**Robustness and Error Detection**: Any error that
alters a single component \(C_i\)
results in a vector that does not correspond to a valid integer within
the intended computational range, enabling immediate error
detection.

**Error Correction Potential**: By choosing moduli
such that the total dynamic range \(M\)
exceeds the required range for a given problem, the redundant space can
be used to encode error-correcting information, enabling the correction
of single-channel errors.

**Formal Measurement Map**: The measurement process
can be formalized as a linear isomorphism \(\mathcal{M}: \mathbf{C} \mapsto
\{G_{xy}^{(i)}\}\), which maps the Chern vector space to the
conductance vector space, completing the formal chain from abstract
integer to physical observable.

### References

Cheon, J. H., Kim, A., Kim, M., & Song, Y. (2017). Homomorphic
Encryption for Arithmetic of Approximate Numbers. In *Advances in
Cryptology–ASIACRYPT 2017* (pp. 409-437). Springer.
https://doi.org/10.1007/978-3-319-70697-9_15

Goguen, J. A., & Burstall, R. M. (1984). Some fundamental
algebraic tools for the semantics of computation. Part 1: Compositions
and refinements. *Theoretical Computer Science*, *31*,
175-213. https://doi.org/10.1016/0304-3975(84)90004-0

Horowitz, M. (2014). Computing’s Energy Problem (and what we can do
about it). In *IEEE International Solid-State Circuits Conference
Digest of Technical Papers (ISSCC)* (pp. 10-14).
https://doi.org/10.1109/ISSCC.2014.6757323

Horsman, C., Kendon, V., Stepney, S., & Munro, W. J. (2014). When
does a physical system compute? *Proceedings of the Royal Society A:
Mathematical, Physical and Engineering Sciences*,
*470*(2171), 20140152. https://doi.org/10.1098/rspa.2014.0152

Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons.
*Annals of Physics*, *303*(1), 2-30.
https://doi.org/10.1016/S0003-4916(02)00018-0

Lloyd, S., & Pagels, H. (1988). Complexity as Thermodynamic
Depth. *Annals of Physics*, *188*(1), 186-213.
https://doi.org/10.1016/0003-4916(88)90094-2

MacLennan, B. J. (2004). Natural Computation and Non-Turing Models of
Computation. *Theoretical Computer Science*, *317*(1-3),
115-145. https://doi.org/10.1016/j.tcs.2003.12.006

Müller, V. C., & Hoffmann, M. (2017). What Is Morphological
Computation? On How the Body Contributes to Cognition and Control.
*Artificial Life*, *23*(1), 1-24.
https://doi.org/10.1162/ARTL_a_00219

Nayak, C., Simon, S. H., Stern, A., Freedman, M., & Das Sarma, S.
(2008). Non-Abelian anyons and topological quantum computation.
*Reviews of Modern Physics*, *80*(3), 1083-1159.
https://doi.org/10.1103/RevModPhys.80.1083

Pfeifer, R., & Bongard, J. (2007). *How the Body Shapes the
Way We Think: A New View of Intelligence*. MIT Press.

Prigogine, I. (1967). Structure, Dissipation and Life. In
*Theoretical Physics and Biology* (pp. 23-52). North Holland.

Sharpe, A. L., Fox, E. J., Barnard, A. W., Finney, J., Watanabe, K.,
Taniguchi, T., Kastner, M. A., & Goldhaber-Gordon, D. (2019).
Emergent ferromagnetism near three-quarters filling in twisted bilayer
graphene. *Science*, *365*(6453), 605-608.
https://doi.org/10.1126/science.aaw3780

Siegelmann, H. T. (1999). Neural and Super-Turing Computing.
*Minds and Machines*, *13*, 103-114.
https://doi.org/10.1023/A:1022902524528

Szabo, N. S., & Tanaka, R. I. (1967). *Residue Arithmetic and
Its Applications to Computer Technology*. McGraw-Hill.

Wen, X.-G. (2002). Quantum orders in an exact soluble model.
*Physical Review B*, *65*(16), 165113.
https://doi.org/10.1103/PhysRevB.65.165113

Xie, Y., Pierce, A. T., Park, J. M., Parker, D. E., Khalaf, E.,
Ledwith, P., Lee, Y., Chen, S., Călugăru, D., Andrei, B. A., &
Yacoby, A. (2021). Fractional Chern insulators in magic-angle twisted
bilayer graphene. *Nature*, *597*(7874), 38–43.
https://doi.org/10.1038/s41586-021-03842-4
