import math

rest_days = int(input())
year = 365
max_norm = 30000
work_day_play_time = 63
rest_day_play_time = 127
work_day = year - rest_days
ttl_play_time = work_day * work_day_play_time + rest_days * rest_day_play_time
diff = abs(ttl_play_time - max_norm)
hrs = math.floor(diff / 60)
min = diff % 60
if ttl_play_time <= max_norm:
    print('Tom sleeps well')
    print(f'{hrs:.0f} hours and {min:.0f} minutes less for play')
elif ttl_play_time > max_norm:
    print('Tom will run away')
    print(f'{hrs:.0f} hours and {min:.0f} minutes more for play')