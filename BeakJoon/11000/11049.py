import sys

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for term in range(1, N):
    for start in range(N):
        end = start + term
        if end >= N:
            break

        dp[start][end] = 2**31

        for mid in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][mid] +
                                 dp[mid+1][end] + A[start][0]*A[mid][1]*A[end][1])

print(dp[0][N-1])
