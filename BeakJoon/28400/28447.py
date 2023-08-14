import sys
from itertools import combinations


def get_taste(comb, C):
    taste = 0
    for i in range(len(comb)):
        for j in range(i + 1, len(comb)):
            taste += C[comb[i]][comb[j]]
    return taste


N, K = map(int, sys.stdin.readline().split())
C = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_taste = float('-inf')
for comb in combinations(range(N), K):
    taste = get_taste(comb, C)
    max_taste = max(max_taste, taste)

print(max_taste)
