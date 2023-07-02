from collections import deque


def BFS(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


total_node = int(input())
edge = int(input())

graph = {i: [] for i in range(1, total_node+1)}

for i in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print(len(BFS(graph, 1))-1)
