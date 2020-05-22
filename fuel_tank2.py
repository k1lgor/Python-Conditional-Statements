t = str(input())
f = float(input())
card = str(input())
if t == 'Gasoline':
    if f > 25:
        if card == 'Yes':
            a = (2.22 - 0.18) * f
            s = a - a * 0.1
            print(f'{s:.2f} lv.')
        else:
            a = 2.22 * f
            s = a - a * 0.1
            print(f'{s:.2f} lv.')
    elif 20 <= f <= 25:
        if card == 'Yes':
            a = (2.22 - 0.18) * f
            s = a - a * 0.08
            print(f'{s:.2f} lv.')
        else:
            a = 2.22 * f
            s = a - a * 0.08
            print(f'{s:.2f} lv.')
    else:
        if card == 'Yes':
            a = (2.22 - 0.18) * f
            print(f'{a:.2f} lv.')
        else:
            a = 2.22 * f
            print(f'{a:.2f} lv.')
if t == 'Diesel':
    if f > 25:
        if card == 'Yes':
            a = (2.33 - 0.12) * f
            s = a - a * 0.1
            print(f'{s:.2f} lv.')
        else:
            a = 2.33 * f
            s = a - a * 0.1
            print(f'{s:.2f} lv.')
    elif 20 <= f <= 25:
        if card == 'Yes':
            a = (2.33 - 0.12) * f
            s = a - a * 0.08
            print(f'{s:.2f} lv.')
        else:
            a = 2.33 * f
            s = a - a * 0.08
            print(f'{s:.2f} lv.')
    else:
        if card == 'Yes':
            a = (2.33 - 0.12) * f
            print(f'{a:.2f} lv.')
        else:
            a = 2.33 * f
            print(f'{a:.2f} lv.')
if t == 'Gas':
    if f > 25:
        if card == 'Yes':
            a = (0.93 - 0.08) * f
            s = a - a * 0.1
            print(f'{s:.2f} lv.')
        else:
            a = 0.93 * f
            s = a - a * 0.1
            print(f'{s:.2f} lv.')
    elif 20 <= f <= 25:
        if card == 'Yes':
            a = (0.93 - 0.08) * f
            s = a - a * 0.08
            print(f'{s:.2f} lv.')
        else:
            a = 0.93 * f
            s = a - a * 0.08
            print(f'{s:.2f} lv.')
    else:
        if card == 'Yes':
            a = (0.93 - 0.08) * f
            print(f'{a:.2f} lv.')
        else:
            a = 0.93 * f
            print(f'{a:.2f} lv.')