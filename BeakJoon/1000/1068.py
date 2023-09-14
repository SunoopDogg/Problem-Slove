import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
del_node = int(sys.stdin.readline())

tree = [[] for _ in range(N)]
for i in range(N):
    if A[i] == -1:
        root = i
    else:
        tree[A[i]].append(i)

if del_node == root:
    print(0)
else:
    cnt = 0
    for i in range(N):
        if del_node in tree[i]:
            tree[i].remove(del_node)

    def dfs(node):
        global cnt
        if not tree[node]:
            cnt += 1
        else:
            for i in tree[node]:
                dfs(i)

    dfs(root)
    print(cnt)
