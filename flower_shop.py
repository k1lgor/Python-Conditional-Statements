import math

mag = int(input())
zum = int(input())
rozi = int(input())
kak = int(input())
gift = float(input())
earn = mag * 3.25 + zum * 4 + rozi * 3.5 + kak * 8
tax = earn * 0.05
ttl_earn = earn - tax
dif = abs(gift - ttl_earn)
if ttl_earn >= gift:
    dif = math.floor(dif)
    print(f'She is left with {dif:.0f} leva.')
else:
    dif = math.ceil(dif)
    print(f'She will have to borrow {dif:.0f} leva.')
