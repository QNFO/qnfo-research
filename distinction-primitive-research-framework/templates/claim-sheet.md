# Claim Sheet Template (DPRF T-1)

Use one sheet per pre-registered claim. Attach to the PROJECT-PLAN core-claim section at P0.
Each row of a disconfirmation matrix is one claim row with these fields.

```markdown
## Claim: <short name>

- **level:** D<0-8> [or span D<X>–D<Y> with bridge list]
- **carrier:** definitional | formal | computational | empirical | engineered
- **ontic_commitment:** methodological (default) | heuristic | ontic
- **map_territory:** map | bridge | territory

<!-- Mandatory iff ontic_commitment=ontic or map_territory ∈ {bridge, territory}: -->
- **protocol:** which observable, on which system, with which instrument, at which resolution
- **null_model:** what the data would look like if the structure were absent
- **falsifier:** the pre-registered observation that would refute the claim

<!-- Recommended for all computational+ carriers: -->
- **reporting_rule:** effect-size commitment; unfolding-sensitivity commitment;
  multiple-comparison correction plan; object-separation statement (e.g., primes vs zeros)

## Bridge list (only if level is a span)

| From | To | Bridge declaration (one sentence) |
|:-----|:---|:----------------------------------|
| D<X> | D<X+1> | ... |
```

## Example (from lineage, post hoc)

- RES.030 D1 discriminability: level D6–D7; carrier computational; ontic methodological;
  map_territory bridge; protocol = specific-heat curve C_V(β) + unfolded two-point statistics on
  the arithmetic cut vs matched-density nulls; null_model = smooth log-spaced surrogates /
  P_max-smooth random integers / Poisson-on-log-scale, matched mean level density; falsifier =
  no observable separates at any feasible P_max (pre-registered; negative branch publishable).
