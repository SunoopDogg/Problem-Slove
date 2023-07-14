import sys
import heapq


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))

start, end = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance[end]


print(dijkstra(start, end))
