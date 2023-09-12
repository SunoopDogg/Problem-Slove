import sys

N, M = map(int, sys.stdin.readline().split())

erdanova_times = [(t, 'E') for t in map(int, sys.stdin.readline().split())]
origin_times = [(t, 'O') for t in map(int, sys.stdin.readline().split())]

events = erdanova_times + origin_times
events.sort()

erdanova_last_use = -100
origin_last_use = -360
erdanova_immune_end = -90
origin_immune_end = -90
erdanova_count = 0
origin_count = 0

for t, skill_type in events:
    if skill_type == 'E':
        if t >= erdanova_last_use + 100 and t > origin_immune_end:
            erdanova_count += 1
            erdanova_last_use = t
            origin_immune_end = t + 90
    else:
        if t >= origin_last_use + 360 and t > erdanova_immune_end:
            origin_count += 1
            origin_last_use = t
            erdanova_immune_end = t + 90

print(erdanova_count, origin_count)
