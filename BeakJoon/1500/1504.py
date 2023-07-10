import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for v, w in graph[node]:
            if dist[v] > cost + w:
                dist[v] = cost + w
                heapq.heappush(q, (dist[v], v))
    return dist


dist1 = dijkstra(1)
dist2 = dijkstra(v1)
dist3 = dijkstra(v2)
answer = min(dist1[v1] + dist2[v2] + dist3[N],
             dist1[v2] + dist3[v1] + dist2[N])
print(answer if answer < float('inf') else -1)
