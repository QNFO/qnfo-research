# ERRATA — The Qudit Advantage (v0.4, DOI 10.5281/zenodo.21827737)

**Status:** Published 2026-08-12 as part of the Corrections and Governance Record
(DOI 10.5281/zenodo.21901930). Supersedes errors in v0.4; corrections applied in the
version chain v0.5 → v0.6 → v0.6.1 → v0.7 (canonical: 10.5281/zenodo.21880104).

## Errors Identified (9 August 2026)

1. **Decoder-energy direction error (§3.3 of v0.4).** The paper set
   `P_decode^qudit ≈ 0`, justified by the algorithmic complexity O(log_p N) of
   tree-traversal decoding, and labeled this a "conservative upper bound." **Correction:**
   zero is a *lower* bound, not an upper bound; the assertion ignores the real classical
   ASIC and control-logic power required to run hierarchical decoders in real time.
2. **Landauer temperature conflation (§3.4 of v0.4).** The bound was computed at room
   temperature (T = 300 K) versus cryogenic temperature (T = 10 mK) in Planck units, and
   erasure-energy floors were conflated with room-temperature operational coherence.
   **Correction:** the Landauer bound is a per-erasure floor; the dominant energy cost is
   active cooling overhead, not erasure energy. No physical hardware mechanism for
   suppressing thermal noise at room temperature was proposed.
3. **Synthetic citation anchors.** Inline keys with custom prefixes (`@C5_jpcub_p0`,
   `@B1_shannon1948`) did not resolve to standard bibliographic entries; the References
   section was empty. **Correction:** all citation anchors replaced with resolvable
   references in subsequent versions.
4. **Self-referential metric.** The performance metric had zero external citations or
   independent validations as of 2026-08-06. **Correction:** this limitation is now stated
   explicitly in the published body.

## Scope

This ERRATA covers the v0.4 text only. Corrections were applied and versioned in v0.5
(10.5281/zenodo.21878856), v0.6 (10.5281/zenodo.21879110), v0.6.1
(10.5281/zenodo.21879117), and the canonical v0.7 (10.5281/zenodo.21880104).
