import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

chicken_comb = list(combinations(chicken, M))
result = sys.maxsize

for comb in chicken_comb:
    temp = 0
    for h in house:
        temp += min([abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in comb])
        if temp > result:
            break
    if temp < result:
        result = temp

print(result)
