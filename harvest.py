import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())
ttl = x * y
wine = ttl * 0.4 / 2.5
diff = abs(wine - z)
if wine < z:
    print(f'It will be a tough winter! More {math.floor(diff):.0f} liters wine needed.')
elif wine >= z:
    print(f'Good harvest this year! Total wine: {math.floor(wine):.0f} liters.')
    wine_for_person = diff / workers
    print(f'{math.ceil(diff):.0f} liters left -> {math.ceil(wine_for_person):.0f} liters per person.')