import sys

N, M, B = map(int, sys.stdin.readline().split())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result, height = int(1e9), 0

for h in range(257):
    min_count, max_count = 0, 0

    for i in range(N):
        for j in range(M):
            if array[i][j] > h:
                max_count += array[i][j] - h
            else:
                min_count += h - array[i][j]

    if max_count + B >= min_count:
        if result >= max_count * 2 + min_count:
            result = max_count * 2 + min_count
            height = h

print(result, height)
