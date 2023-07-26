import sys

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0 for _ in range(N+1)]
parent[1] = 1

stack = [1]

while stack:
    node = stack.pop()
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            stack.append(i)

for i in range(2, N+1):
    print(parent[i])
