import sys
sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)


visited = [False] * (N+1)
dp = [0] * (N+1)


def dfs(node):
    visited[node] = True
    dp[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dp[node] += dfs(i)
    return dp[node]


dfs(R)

for _ in range(Q):
    print(dp[int(sys.stdin.readline())])
