import sys
import fractions

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

if len(sys.argv) < 3:
    exit()
m = int(sys.argv[1])
TARGET = int(sys.argv[2])

p_list = [1.0/32, 1.0/64, 1.0/128, 1.0/256, 1.0/512, 1.0/1024, 1.0/2048, 
            1.0/4096, 1.0/8192, 1.0/16384]
min_re = 0x1f1f1f1f
min_var = 0
min_config = None
n = m
for p in p_list:
    if p > float(1.0/m):
        continue
    var = 0
    target = 0
    for i in range(n):
        P = p * (m - i)
        target += 1.0/P
        var += (1-P)/(P**2)
    std_var = pow(var, 0.5)
    std_var_ratio = std_var / TARGET
    RE = abs(TARGET - target) / TARGET
    if RE <= min_re and std_var_ratio < 0.3:
        min_re = RE
        min_var = std_var
        min_config = (m, n, fractions.Fraction(p))
print(min_config, min_re, min_var)