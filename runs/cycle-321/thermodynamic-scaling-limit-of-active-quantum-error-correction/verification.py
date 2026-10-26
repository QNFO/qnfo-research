import math

def fmt(v):
    # format with up to 8 significant digits, removing trailing zeros
    s = f"{v:.8g}"
    return s

claims = [
    # Q1
    ("Q1", (0.3 * 1e4) / (1e6 * 1e-9), "3×10⁶"),
    # Q2
    ("Q2", 1e6 * 1e-9, "1.0×10⁻³ W"),
    # Q3
    ("Q3", 0.3 * 1e4, "3.0×10³ W·m⁻²"),
    # Q4
    ("Q4", 1.0 / (1e-4 ** 2), "1×10⁸ m⁻²"),
    # Q5
    ("Q5", (1e6 * 1e-9) / ((1e-4) ** 2 * 1e4), "10 K"),
    # Q6
    ("Q6", (1e-6 ** 2) * 1e-2, "1×10⁻¹⁴ W"),
    # Q7
    ("Q7", (1e8) / (3e6), "approximately 33"),
    # Q8
    ("Q8", (0.3 * 3e4) / (1e6 * 1e-9), "9×10⁶ m⁻²"),
    # Q9
    ("Q9", (1e6 * 1e-9) / ((1e-4) ** 2 * 3e4), "3.33 K"),
    # Q10
    ("Q10", (1e8) / (9e6), "≈11×"),
    # Q11
    ("Q11", (0.3 * 1e4) / (1e6 * 1e-11), "3×10⁸ m⁻²"),
    # Q12
    ("Q12", (1e6 * 1e-11) / ((1e-4) ** 2 * 1e4), "0.10 K"),
    # Q13
    ("Q13", math.sqrt((1e6 * 1e-9) / (0.3 * 1e4)), "5.77×10⁻⁴ m (≈580 µm)"),
    # Q14
    ("Q14", 0.5e6 * 1e-11, "5.0×10⁻⁶ W"),
    # Q15
    ("Q15", (0.3 * 1e4) / (0.5e6 * 1e-11), "6×10⁸ m⁻²"),
    # Q16
    ("Q16", (0.5e6 * 1e-11) / ((1e-4) ** 2 * 1e4), "5.0×10⁻⁶ K"),
]

def match(computed, expected):
    # simple matching rules for the expected strings used in the paper
    if expected.startswith("approximately"):
        # compare rounded integer
        target = int(expected.split()[-1])
        return round(computed) == target
    if expected.startswith("≈"):
        # compare rounded integer after the symbol
        target = int(expected[1:-1])  # remove ≈ and trailing ×
        return round(computed) == target
    # for scientific notation strings, compare after converting both to float
    # replace unicode superscripts and symbols
    exp_clean = expected.replace('×10⁶', 'e6').replace('×10⁻³', 'e-3')\
                        .replace('×10³', 'e3').replace('×10⁸', 'e8')\
                        .replace('×10⁻⁴', 'e-4').replace('×10⁻⁶', 'e-6')\
                        .replace('×10⁻¹⁴', 'e-14').replace('×10⁻⁹', 'e-9')\
                        .replace('×10⁻¹¹', 'e-11').replace('×10⁻⁶', 'e-6')
    try:
        expected_val = float(exp_clean.split()[0])
        # compare within 1% relative tolerance
        return abs(computed - expected_val) / expected_val < 0.01
    except:
        # fallback: exact string match after formatting
        return fmt(computed) == expected

for cid, comp, exp in claims:
    m = "yes" if match(comp, exp) else "no"
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={m}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if match(c,e))} match, {sum(1 for _,c,e in claims if not match(c,e))} mismatch")
