import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    degree[b] += 1


q = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=' ')

    for i in graph[now]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
