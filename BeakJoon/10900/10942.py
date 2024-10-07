import sys
sys.setrecursionlimit(10**6)


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())


memo = [[-1] * N for _ in range(N)]
for i in range(N):
    memo[i][i] = 1
    if i < N - 1:
        if A[i] == A[i + 1]:
            memo[i][i + 1] = 1
        else:
            memo[i][i + 1] = 0


def dp(start, end):
    if start > end:
        return 1
    if memo[start][end] != -1:
        return memo[start][end]

    if A[start] != A[end]:
        memo[start][end] = 0
        return 0

    memo[start][end] = dp(start + 1, end - 1)
    return memo[start][end]


for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp(S - 1, E - 1))
