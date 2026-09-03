import math
k_B = 1.380649e-23
ln2 = math.log(2)
def surface_code(d):
    n_c = 2*d*d - 1
    return n_c, (8*d*d)*d
def landauer(T): return k_B * T * ln2
def ml_time(f): return 1.0/(4.0*f)
print('=== NV.001 surface-code energy per logical operation ===')
for T in [300.0, 77.0, 4.0, 0.02]: print('  T=%8.2f K -> %.3e J/bit' % (T, landauer(T)))
rows = []
for d in [3,5,7,9,11,15,21,31]:
    nc, ng = surface_code(d); rows.append((d,nc,ng))
    print('  d=%2d N_c=%5d N_g=%8d E(1pJ)=%.3e E_L(300K)=%.3e E_L(4K)=%.3e' % (d,nc,ng,ng*1e-12,ng*landauer(300.0),ng*landauer(4.0)))
print('Scaling: N_g(15)/N_g(9)=%.4f (15/9)^3=%.4f  |  N_g(21)/N_g(9)=%.4f (21/9)^3=%.4f' % (rows[5][2]/rows[3][2],(15.0/9.0)**3,rows[6][2]/rows[3][2],(21.0/9.0)**3))
print('=== NV.002 Margolus-Levitin bound + crossover ===')
for f in [1e6,1e7,1e8,1e9]: print('  gap=%8.0e Hz -> t_ML = %.3e s' % (f, ml_time(f)))
for gamma in [1e6,1e8,1e9]:
    T2 = 1.0/gamma
    for f in [1e7,1e9]:
        tml = ml_time(f); regime = 'decoherence-bound' if T2 < tml else 'speed-limit-bound'
        print('  Gamma=%8.0e T2=%.3e gap=%8.0e t_ML=%.3e -> %s' % (gamma,T2,f,tml,regime))
print('=== NV.003 Landauer floor + ratio ===')
for d in [7,11]:
    nc, ng = surface_code(d)
    print('  d=%2d N_g=%8d E_min(4K)=%.3e E_real(1pJ)=%.3e ratio=%.1e' % (d,ng,ng*landauer(4.0),ng*1e-12,(ng*1e-12)/(ng*landauer(4.0))))
print('=== NV.004 overhead normalization ===')
for d in [3,5,9,15,21]:
    nc, ng = surface_code(d)
    print('  d=%2d N_c=%5d N_g/logical-op=%8d log10=%.2f' % (d,nc,ng,math.log10(ng)))
print('=== NV.005 latency-energy product ===')
prod = []
for d in [3,5,9,15,21,31]:
    nc, ng = surface_code(d); t = d*1e-6; E = ng*1e-12; prod.append(t*E)
    print('  d=%2d t=%.2e E=%.3e E*t=%.3e' % (d,t,E,t*E))
print('product ratio (31/3): %.3e vs (31/3)^4=%.3e' % (prod[-1]/prod[0],(31.0/3.0)**4))