import sys
import bisect

N, M = map(int, sys.stdin.readline().split())

if N <= M:
    smaller_team = list(map(int, sys.stdin.readline().split()))
    larger_team = sorted(list(map(int, sys.stdin.readline().split())))
    flip = False
else:
    larger_team = sorted(list(map(int, sys.stdin.readline().split())))
    smaller_team = list(map(int, sys.stdin.readline().split()))
    flip = True

smaller_win, draw = 0, 0

for skill in smaller_team:
    idx_left = bisect.bisect_left(larger_team, skill)
    idx_right = bisect.bisect_right(larger_team, skill)

    smaller_win += len(larger_team) - idx_left

    draw_count = idx_right - idx_left
    if draw_count:
        smaller_win -= draw_count
        draw += draw_count

larger_win = N * M - (smaller_win + draw)

if flip:
    print(smaller_win, larger_win, draw)
else:
    print(larger_win, smaller_win, draw)
