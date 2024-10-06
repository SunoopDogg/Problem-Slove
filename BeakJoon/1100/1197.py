import sys
sys.setrecursionlimit(10**6)

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A - 1].append((B - 1, C))


def kruskal():
    edges = []
    for i in range(V):
        for j in range(len(graph[i])):
            edges.append((graph[i][j][1], i, graph[i][j][0]))
    edges.sort()

    parent = [i for i in range(V)]

    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


print(kruskal())
