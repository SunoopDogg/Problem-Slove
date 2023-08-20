import sys

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))

graph = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if graph[i][j] <= m:
            temp += items[j]
    result = max(result, temp)

print(result)
