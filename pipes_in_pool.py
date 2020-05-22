v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
P1 = p1 * h
P2 = p2 * h
pp = P1 + P2
if pp <= v:
    V = pp / v * 100
    pp1 = P1 / pp * 100
    pp2 = P2 / pp * 100
    print(f'The pool is {V:.2f}% full. Pipe 1: {pp1:.2f}%. Pipe 2: {pp2:.2f}%.')
elif pp > v:
    over = abs(v - pp)
    print(f'For {h} hours the pool overflows with {over:.2f} liters.')