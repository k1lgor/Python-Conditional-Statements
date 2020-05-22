type = str(input())
q = float(input())
if type == 'Diesel':
    if q >= 25:
        print(f'You have enough {type.lower()}.')
    else:
        print(f'Fill your tank with {type.lower()}!')
elif type == 'Gasoline':
    if q >= 25:
        print(f'You have enough {type.lower()}.')
    else:
        print(f'Fill your tank with {type.lower()}!')
elif type == 'Gas':
    if q >= 25:
        print(f'You have enough {type.lower()}.')
    else:
        print(f'Fill your tank with {type.lower()}!')
else:
    print('Invalid fuel!')