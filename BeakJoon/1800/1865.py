import sys


def bellman_ford(graph, start):
    dist = [sys.maxsize] * len(graph)
    dist[start] = 0
    for _ in range(len(graph) - 1):
        for v in range(1, len(graph)):
            for nv, w in graph[v]:
                if dist[nv] > dist[v] + w:
                    dist[nv] = dist[v] + w
    for v in range(1, len(graph)):
        for nv, w in graph[v]:
            if dist[nv] > dist[v] + w:
                return True
    return False


TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        graph[S].append((E, -T))

    if bellman_ford(graph, 1):
        print("YES")
    else:
        print("NO")
