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
