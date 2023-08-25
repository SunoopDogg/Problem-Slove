import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(sys.stdin.readline())

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i - 1]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i - 1])

            if indegree[i] == 0:
                q.append(i)

    print(dp[W])
