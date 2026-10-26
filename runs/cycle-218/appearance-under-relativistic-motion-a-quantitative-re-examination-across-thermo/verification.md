# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The Lorentz factor at the benchmark speed β₁=0.8 is γ₁=5/3≈1.666667.",
    "inputs": "β₁ = 0.8",
    "formula": "γ = 1 / sqrt(1 - β^2)"
  },
  {
    "id": "Q2",
    "statement": "The longitudinal Doppler factor for an approaching observer at β₁=0.8 is D₊=3.",
    "inputs": "γ₁ = 5/3, β₁ = 0.8",
    "formula": "D₊ = 1 / (γ * (1 - β))"
  },
  {
    "id": "Q3",
    "statement": "The longitudinal Doppler factor for a receding observer at β₁=0.8 is D₋=1/3.",
    "inputs": "γ₁ = 5/3, β₁ = 0.8",
    "formula": "D₋ = 1 / (γ * (1 + β))"
  },
  {
    "id": "Q4",
    "statement": "The transverse Doppler factor at β₁=0.8 is D⊥=1/γ₁=0.6.",
    "inputs": "γ₁ = 5/3",
    "formula": "D⊥ = 1 / γ"
  },
  {
    "id": "Q5a",
    "statement": "The “cooler” temperature‑transformation candidate gives T_cool = T₀/γ₁ = 0.6 T₀.",
    "inputs": "γ₁ = 5/3",
    "formula": "T_cool = T₀ / γ"
  },
  {
    "id": "Q5b",
    "statement": "The “hotter” temperature‑transformation candidate gives T_hot = γ₁ T₀ = 1.666667 T₀.",
    "inputs": "γ₁ = 5/3",
    "formula": "T_hot = γ * T₀"
  },
  {
    "id": "Q5c",
    "statement": "The ratio of the hotter to cooler candidate temperatures is γ₁² = 25/9 ≈ 2.777778.",
    "inputs": "γ₁ = 5/3",
    "formula": "ratio = γ²"
  },
  {
    "id": "Q6",
    "statement": "The apparent temperature in the forward direction (θ=0) is T_app = 3 T₀.",
    "inputs": "D₊ = 3, T₀ (symbolic)",
    "formula": "T_app = D * T₀"
  },
  {
    "id": "Q7",
    "statement": "The apparent temperature in the backward direction (θ=π) is T_app = T₀/3.",
    "inputs": "D₋ = 1/3, T₀ (symbolic)",
    "formula": "T_app = D * T₀"
  },
  {
    "id": "Q8",
    "statement": "The solid‑angle‑averaged apparent temperature of an isotropic blackbody field at β₁=0.8 is ̅T = 0.8240 T₀ (17.6 % cooling).",
    "inputs": "β₁ = 0.8, γ₁ = 5/3, atanh(0.8) = 1.0986",
    "formula": "⟨T⟩ = T₀ * atanh(β) / (γ * β)"
  },
  {
    "id": "Q9",
    "statement": "The radiation‑pressure force per area on a receding perfect mirror at β₁=0.8 is F₁/A = 0.1778 u₀.",
    "inputs": "β₁ = 0.8, u₀ (symbolic)",
    "formula": "F/A = u₀ * 2β(1-β) / (1+β)"
  },
  {
    "id": "Q10",
    "statement": "For a static mirror the radiation‑pressure force per area is F₀/A = 2 u₀.",
    "inputs": "u₀ (symbolic)",
    "formula": "F₀/A = 2 * u₀"
  },
  {
    "id": "Q11",
    "statement": "The suppression factor for the moving mirror relative to the static case is 0.0889 (an 89.1 % reduction).",
    "inputs": "F₁/A = 0.1778 u₀, F₀/A = 2 u₀",
    "formula": "suppression = (F₁/A) / (F₀/A)"
  },
  {
    "id": "Q12",
    "statement": "The Jüttner‑tail suppression factor for k_B T₀ = 0.1 m c² and γ_p = 2 is e^{‑10} = 4.5400×10⁻⁵.",
    "inputs": "k_B T₀ = 0.1 m c², γ_p = 2",
    "formula": "weight ratio = exp[-(γ_p - 1) / (k_B T₀ / (m c²))]"
  },
  {
    "id": "Q13",
    "statement": "The speed that yields a forward Doppler factor D = 10 is β = 99/101 ≈ 0.9802.",
    "inputs": "D = 10",
    "formula": "β = (D² - 1) / (D² + 1)"
  },
  {
    "id": "Q14",
    "statement": "For the re‑entry scenario with β = 0.9 the Lorentz factor is γ = 2.2942.",
    "inputs": "β = 0.9",
    "formula": "γ = 1 / sqrt(1 - β²)"
  }
]

## Script
```python
import math

def compare(computed, expected_str):
    # Remove whitespace
    expected = expected_str.strip()
    # Try to compare as float if possible
    try:
        expected_val = float(expected)
        # Determine number of significant digits in expected
        # Count digits after decimal if '.' present, else count total digits
        if '.' in expected:
            # Count total digits after decimal ignoring trailing zeros
            after = expected.split('.')[1]
            sig_digits = len(after.rstrip('0'))
        else:
            # No decimal point, treat as integer
            sig_digits = len(expected.lstrip('0'))
        # Round computed to same number of decimal places as expected
        if '.' in expected:
            places = len(after)
            comp_rounded = round(computed, places)
        else:
            comp_rounded = round(computed)
        match = (abs(comp_rounded - expected_val) < 1e-12)
        return f"{comp_rounded}", match
    except ValueError:
        # Expected is not a plain number (e.g., a fraction); compare string representation
        comp_str = f"{computed:.6f}"
        match = (comp_str == expected)
        return comp_str, match

# Claims
claims = [
    ("Q1", 1 / math.sqrt(1 - 0.8**2), "1.666667"),
    ("Q2", 1 / ((5/3) * (1 - 0.8)), "3"),
    ("Q3", 1 / ((5/3) * (1 + 0.8)), "0.333333"),
    ("Q4", 1 / (5/3), "0.6"),
    ("Q5a", 1 / (5/3), "0.6"),
    ("Q5b", (5/3), "1.666667"),
    ("Q5c", (5/3)**2, "2.777778"),
    ("Q6", 3, "3"),
    ("Q7", 1/3, "0.333333"),
    ("Q8", (math.atanh(0.8) / ((5/3) * 0.8)), "0.8240"),
    ("Q9", (2 * 0.8 * (1 - 0.8) / (1 + 0.8)), "0.1778"),
    ("Q10", 2, "2"),
    ("Q11", (0.17777777777777778) / 2, "0.0889"),
    ("Q12", math.exp(-10), "4.5400e-05"),
    ("Q13", (10**2 - 1) / (10**2 + 1), "0.9802"),
    ("Q14", 1 / math.sqrt(1 - 0.9**2), "2.2942"),
]

for cid, value, expected in claims:
    comp_str, match = compare(value, expected)
    print(f"CLAIM {cid}: computed={comp_str} expected={expected} match={'yes' if match else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, {} match, {} mismatch".format(
    sum(1 for _,_,e in claims if compare(_, e)[1]),
    sum(1 for _,_,e in claims if not compare(_, e)[1])
))

```

## Execution output
```
CLAIM Q1: computed=1.666667 expected=1.666667 match=yes
CLAIM Q2: computed=3 expected=3 match=yes
CLAIM Q3: computed=0.333333 expected=0.333333 match=yes
CLAIM Q4: computed=0.6 expected=0.6 match=yes
CLAIM Q5a: computed=0.6 expected=0.6 match=yes
CLAIM Q5b: computed=1.666667 expected=1.666667 match=yes
CLAIM Q5c: computed=2.777778 expected=2.777778 match=yes
CLAIM Q6: computed=3 expected=3 match=yes
CLAIM Q7: computed=0.333333 expected=0.333333 match=yes
CLAIM Q8: computed=0.824 expected=0.8240 match=yes
CLAIM Q9: computed=0.1778 expected=0.1778 match=yes
CLAIM Q10: computed=2 expected=2 match=yes
CLAIM Q11: computed=0.0889 expected=0.0889 match=yes
CLAIM Q12: computed=4.54e-05 expected=4.5400e-05 match=yes
CLAIM Q13: computed=0.9802 expected=0.9802 match=yes
CLAIM Q14: computed=2.2942 expected=2.2942 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.666667 | 1.666667 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.333333 | 0.333333 | yes | match | 6 significant digits (as printed, at least 3) |
| Q4 | 0.6 | 0.6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5a | 0.6 | 0.6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5b | 1.666667 | 1.666667 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5c | 2.777778 | 2.777778 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 0.333333 | 0.333333 | yes | match | 6 significant digits (as printed, at least 3) |
| Q8 | 0.824 | 0.8240 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.1778 | 0.1778 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 2 | 2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.0889 | 0.0889 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 4.54e-05 | 4.5400e-05 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 0.9802 | 0.9802 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 2.2942 | 2.2942 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
