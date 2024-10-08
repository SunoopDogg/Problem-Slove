from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[] * N for _ in range(N)]
edges = [0 for _ in range(N)]

for _ in range(M):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(2, len(arr)):
        graph[arr[i - 1] - 1].append(arr[i] - 1)
        edges[arr[i] - 1] += 1

node = [0 for _ in range(N)]
result = []

queue = deque()
for i in range(N):
    if edges[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()

    if node[cur] == 1:
        result = [0]
        break

    result.append(cur + 1)
    node[cur] = 1

    for i in graph[cur]:
        edges[i] -= 1
        if edges[i] == 0:
            queue.append(i)

if len(result) != N:
    print(0)
else:
    print(*result, sep='\n')
