import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


def dijkstra(start):
    dist = [sys.maxsize] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        w, u = heapq.heappop(heap)
        if dist[u] < w:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist


dist = [0] * (N + 1)
for i in range(1, N + 1):
    dist[i] = dijkstra(i)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, dist[i][X] + dist[X][i])
print(answer)
