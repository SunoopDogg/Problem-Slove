import sys

V = int(sys.stdin.readline())

tree = [[] for _ in range(V+1)]
for _ in range(V):
    node = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(node)-1, 2):
        tree[node[0]].append((node[i], node[i+1]))


def dfs(start):
    visited = [False] * (V+1)
    stack = [(start, 0)]
    max_node = [0, 0]
    while stack:
        node, cost = stack.pop()
        visited[node] = True
        if max_node[1] < cost:
            max_node = node, cost
        for next_node, next_cost in tree[node]:
            if not visited[next_node]:
                stack.append((next_node, cost + next_cost))
    return max_node


node, cost = dfs(1)
node, cost = dfs(node)
print(cost)
