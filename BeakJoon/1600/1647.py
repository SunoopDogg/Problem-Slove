import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x


N, M = map(int, sys.stdin.readline().split())
edge = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edge.append((C, A, B))

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

edge.sort()
result = 0
last = 0
for e in edge:
    cost, a, b = e
    if find(a) != find(b):
        union(a, b)
        result += cost
        last = cost

print(result - last)
