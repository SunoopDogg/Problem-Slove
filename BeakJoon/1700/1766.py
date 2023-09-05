import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

problem = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
heap = []
result = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    problem[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for i in problem[data]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

print(*result)
