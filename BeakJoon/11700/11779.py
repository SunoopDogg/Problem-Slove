import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
start, end = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))

    distance = [float('inf')] * (n+1)
    distance[start] = 0
    path = [start] * (n+1)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for e, w in graph[now]:
            cost = dist + w

            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))
                path[e] = now

    temp = end
    result = [end]
    while temp != start:
        result.append(path[temp])
        temp = path[temp]

    print(distance[end])
    print(len(result))
    print(*result[::-1])


dijkstra(start, end)
