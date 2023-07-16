import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p-1].append((c-1, w))
    tree[c-1].append((p-1, w))


def dfs(start):
    stack = [(start, 0)]
    visited = [False] * n
    visited[start] = True
    max_node, max_weight = 0, 0
    while stack:
        node, weight = stack.pop()
        if max_weight < weight:
            max_node, max_weight = node, weight
        for next_node, next_weight in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, weight + next_weight))

    return max_node, max_weight


node, _ = dfs(0)
_, weight = dfs(node)
print(weight)
