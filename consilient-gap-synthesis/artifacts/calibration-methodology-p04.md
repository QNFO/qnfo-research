# Calibration Methodology — Extracted for P-04 Reuse

**Source:** continuum-trilogy `artifacts/phase4-likelihood-calibration.md` (Phase 4 Stage -1)  
**Target:** P-04 — biophoton Calibration Training (biophoton-ultrametric-consilience)  
**Extracted:** 2026-07-30  

---

## 1. Overview — The KIF-31 Likelihood Calibration Protocol

Per KIF-31, every P(E|H) likelihood > 0.80 assigned in a Bayesian cascade
MUST trace to at least one empirical calibration pillar. Without this, precise
decimals communicate false quantitative precision for what are fundamentally
directional human intuitions.

## 2. Calibration Pillars (5 types)

| Pillar | Operational Definition | Constraint |
|:-------|:----------------------|:-----------|
| **Empirical Base Rate** | Search literature for how often claims of this type resolve to confirmed findings. Cite at least one meta-analysis or systematic review. | Value in [baseRate × 0.5, baseRate × 2.0] |
| **Reference-Class Forecast** | Identify ≥3 closest historical scientific predictions of same type, magnitude, and maturity as the target claim. Record actual outcomes. | Likelihood anchored to reference-class range |
| **Calibrated Subjective Confidence** | Before assigning any likelihood, complete ≥20 everyday-quantity questions (90% confidence intervals). Measure personal Brier score / overconfidence error. | If overconfidence > 0.15 Brier, adjust all >0.80 likelihoods downward by factor (1.0 − overconfidence_error) |
| **Inter-Rater Reliability** | Independent REVIEWER subagent assigns same likelihood without seeing primary agent's value. Report divergence. | If divergence > 0.15, use MORE CONSERVATIVE value |
| **Known Prior** | Peer-reviewed empirical estimate exists (e.g., "discover 10 GeV SUSY" has peer-reviewed prior from LHC null results). | Use directly. No adjustment. |

## 3. Protocol (Steps 1-5)

### Step 1: Identify Triggers
For every assumption with P > 0.80, identify which pillar(s) apply.

### Step 2: Run Calibration Training
≥20-question confidence interval quiz. Measure Brier score.
- If Brier > 0.15 → apply overconfidence adjustment to ALL >0.80 likelihoods.

### Step 3: Inter-Rater Reliability
Delegate same assumptions to REVIEWER subagent.
- If divergence > 0.15 → use conservative value, flag disagreement.

### Step 4: Cap Unanchored Likelihoods
Any raw likelihood > 0.80 that CANNOT be anchored to an empirical pillar:
→ **cap at 0.80** with tag `[CALIBRATION-CAP: no empirical pillar]`

### Step 5: Produce Calibration Audit
Output `artifacts/likelihood-calibration.md` with calibrated values.

## 4. Calibration Audit Template

```markdown
# Likelihood Calibration Audit: {project-slug}

## Assumption H1: {short statement}

| Parameter | Raw Estimate | Pillar | Anchor / Rationale | Calibrated |
|:----------|:-------------|:-------|:-------------------|:-----------|
| P(E1|H1) | 0.90 | Empirical Base Rate | {citation}: X/Y claims → base rate Z | 0.75 |
| P(E1|¬H1) | 0.20 | Reference Class | {3 historical cases} | 0.15 |

## Calibration Training Results
Brier score: {value} | Overconfidence error: {value} | Adjustment factor: {value}

## Inter-Rater Reliability
| Assumption | Agent Value | Reviewer Value | Divergence | Resolution |
|:-----------|:------------|:---------------|:-----------|:-----------|
| H1 E1 | 0.90 (raw) | 0.72 | 0.18 | Conservative used |
```

## 5. Integration with Bayesian Cascade

- **Stage -1** (Calibration): Produces calibrated likelihoods — the ONLY values that enter Stage 2.
- **Stage 2** (Assumption Audit): Uses calibrated values from Stage -1.
- **Stage 4** (Sensitivity): Span-based sensitivity from calibration pillar bounds.
- **Stage 5** (Register): [STRONG] / [WEAK] tags based on which pillar anchored.

## 6. P-04 Application

P-04 (biophoton Calibration Training) needs:
1. Identify >0.80 likelihoods in biophoton Bayesian cascade
2. Run calibration training (Brier score measurement)
3. REVIEWER subagent inter-rater assessment
4. Cap/correct unanchored likelihoods
5. Document in `artifacts/likelihood-calibration.md`

**Estimated effort:** 1 session (M). All methodology is proven — needs biophoton domain data.
