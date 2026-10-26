import math

# Q1
H = 2**50
expected_Q1 = "1.1259e15"
print(f"CLAIM Q1: computed={H:.6g} expected={expected_Q1} match={'yes' if f'{H:.6g}'==expected_Q1 else 'no'}")

# Q2
R = 50*49//2
expected_Q2 = "1225"
print(f"CLAIM Q2: computed={R} expected={expected_Q2} match={'yes' if str(R)==expected_Q2 else 'no'}")

# Q3
rho = H / R
expected_Q3 = "9.19e11"
print(f"CLAIM Q3: computed={rho:.3e} expected={expected_Q3} match={'yes' if f'{rho:.3e}'==expected_Q3 else 'no'}")

# Q4
memory_H = 16 * 2**50
memory_H_PB = memory_H / 1e15
expected_Q4 = "18.014"
print(f"CLAIM Q4: computed={memory_H_PB:.3f} expected={expected_Q4} match={'yes' if f'{memory_H_PB:.3f}'==expected_Q4 else 'no'}")

# Q5
memory_R = 16 * R
expected_Q5 = "1.96e4"
print(f"CLAIM Q5: computed={memory_R:.2e} expected={expected_Q5} match={'yes' if f'{memory_R:.2e}'==expected_Q5 else 'no'}")

# Q6
sigma_low = 0.005 / 2.354820
expected_Q6 = "2.1233e-3"
print(f"CLAIM Q6: computed={sigma_low:.4e} expected={expected_Q6} match={'yes' if f'{sigma_low:.4e}'==expected_Q6 else 'no'}")

# Q7
sigma_high = 0.01 / 2.354820
expected_Q7 = "4.2466e-3"
print(f"CLAIM Q7: computed={sigma_high:.4e} expected={expected_Q7} match={'yes' if f'{sigma_high:.4e}'==expected_Q7 else 'no'}")

# Q8
epsilon_wc = 5 * 1e-2
expected_Q8 = "5e-2"
print(f"CLAIM Q8: computed={epsilon_wc:.2e} expected={expected_Q8} match={'yes' if f'{epsilon_wc:.2e}'==expected_Q8 else 'no'}")

# Q9
epsilon_rss = math.sqrt(5) * 1e-2
expected_Q9 = "2.2361e-2"
print(f"CLAIM Q9: computed={epsilon_rss:.4e} expected={expected_Q9} match={'yes' if f'{epsilon_rss:.4e}'==expected_Q9 else 'no'}")

# Q10
ratio = math.sqrt(5)
expected_Q10 = "2.2361"
print(f"CLAIM Q10: computed={ratio:.4f} expected={expected_Q10} match={'yes' if f'{ratio:.4f}'==expected_Q10 else 'no'}")

# Q11
Tf = 1/90
expected_Q11 = "0.011111 s = 11.111 ms"
computed_Q11 = f"{Tf:.6f} s = {Tf*1000:.3f} ms"
print(f"CLAIM Q11: computed={computed_Q11} expected={expected_Q11} match={'yes' if computed_Q11==expected_Q11 else 'no'}")

# Q12
percentage = (Tf*1000) / 20 * 100  # using ms values
expected_Q12 = "55.6%"
print(f"CLAIM Q12: computed={percentage:.1f}% expected={expected_Q12} match={'yes' if f'{percentage:.1f}%'==expected_Q12 else 'no'}")

# Q13
theta_blur = 360 * 1 * Tf
expected_Q13 = "4.0"
print(f"CLAIM Q13: computed={theta_blur:.1f} expected={expected_Q13} match={'yes' if f'{theta_blur:.1f}'==expected_Q13 else 'no'}")

# Q14
theta_sample_60 = 360 / 60
expected_Q14 = "6.0"
print(f"CLAIM Q14: computed={theta_sample_60:.1f} expected={expected_Q14} match={'yes' if f'{theta_sample_60:.1f}'==expected_Q14 else 'no'}")

# Q15
theta_sample_1000 = 360 / 1000
expected_Q15 = "0.36"
print(f"CLAIM Q15: computed={theta_sample_1000:.2f} expected={expected_Q15} match={'yes' if f'{theta_sample_1000:.2f}'==expected_Q15 else 'no'}")

# Q16
ratio_ang = theta_sample_60 / theta_sample_1000
expected_Q16 = "16.7"
print(f"CLAIM Q16: computed={ratio_ang:.1f} expected={expected_Q16} match={'yes' if f'{ratio_ang:.1f}'==expected_Q16 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")
