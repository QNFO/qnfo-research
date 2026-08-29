# Gate Checklist (DPRF T-3, executable)

Run per claim, per audit pass, and per publication gate review.

## G1 — ONTIC-GATE

- [ ] `ontic_commitment` declared on the claim row (default `methodological`).
- [ ] If `ontic`: commitment is per claim, explicit in prose, and justified.
- [ ] If `ontic`: G2 triple present and pre-registered with the claim (not retrofitted).
- [ ] Prose scan: no sentence uses the distinction language with ontic force outside a declared
      ontic commitment ("the universe is made of cuts" ⇒ violation unless declared).

## G2 — REALIZATION-GATE

- [ ] `map_territory` declared (`map` / `bridge` / `territory`).
- [ ] If `bridge` or `territory`: `protocol` names observable, system, instrument, resolution.
- [ ] If `bridge` or `territory`: `null_model` says what absent-structure data look like
      (matched-density nulls for spectral claims).
- [ ] If `bridge` or `territory`: `falsifier` is pre-registered and would actually refute.
- [ ] Reporting: effect sizes, not only p-values; ≥ 3 unfoldings; pre-registered multiplicity
      correction; object separation (primes vs zeros; two-point vs one-point).

## Level discipline (R1–R5)

- [ ] Level or span declared (R1).
- [ ] Cross-level moves carry a declared bridge per step (R2, R3).
- [ ] Downward moves labeled interpretation, not derivation (R4).
- [ ] No level/object conflation (R5).

## Verdict line

```
claim=<name> level=<DX> gates=G1:PASS,G2:PASS defects=0
```
