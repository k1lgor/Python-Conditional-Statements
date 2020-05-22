import math

hrs_needed = int(input())
limit_days = int(input())
workers_out = int(input())
work_hrs = (limit_days - limit_days * 0.1) * 8
workers_hrs_out = math.floor(workers_out * 2 * limit_days)
ttl_work_hrs = math.floor(work_hrs + workers_hrs_out)
dif = abs(ttl_work_hrs - hrs_needed)
if ttl_work_hrs >= hrs_needed:
    print(f'Yes!{dif:.0f} hours left.')
else:
    print(f'Not enough time!{dif:.0f} hours needed.')