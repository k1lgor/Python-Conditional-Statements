km = int(input())
name = str(input())
if km >= 100:
    if name == 'day':
        a = km * 0.06
        print(f'{a:.2f}')
    else:
        a = km * 0.06
        print(f'{a:.2f}')
elif 20 <= km <= 100:
    if name == 'day':
        a = km * 0.09
        print(f'{a:.2f}')
    else:
        a = km * 0.09
        print(f'{a:.2f}')
else:
    if name == 'day':
        a = 0.7 + km * 0.79
        print(f'{a:.2f}')
    else:
        a = 0.7 + km * 0.9
        print(f'{a:.2f}')