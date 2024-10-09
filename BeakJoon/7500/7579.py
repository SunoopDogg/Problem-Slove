import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))
C = [0] + list(map(int, sys.stdin.readline().split()))


dp = [[0] * (sum(C) + 1) for _ in range(N + 1)]
result = int(1e9)


for i in range(1, N + 1):
    for j in range(sum(C) + 1):
        temp_m = A[i]
        temp_c = C[i]

        if j < C[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - temp_c] + temp_m)

        if dp[i][j] >= M:
            result = min(result, j)

print(result)
