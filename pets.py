import math

days = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
trtl_food = float(input())
ttl_food = dog_food * days + cat_food * days + trtl_food * days / 1000
dif = abs(ttl_food - food_left)
if ttl_food <= food_left:
    dif = math.floor(dif)
    print(f'{dif:.0f} kilos of food left.')
else:
    dif = math.ceil(dif)
    print(f'{dif:.0f} more kilos of food are needed.')