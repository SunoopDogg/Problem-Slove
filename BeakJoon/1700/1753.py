import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


def dijkstra(start):
    distance = [float('inf')] * (V + 1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for v, w in graph[node]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))
    return distance


for d in dijkstra(K)[1:]:
    print(d if d != float('inf') else 'INF')
