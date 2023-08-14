import sys

N, M = map(int, sys.stdin.readline().split())

map_data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
H = int(sys.stdin.readline())

dp = [[float('inf')] * M for _ in range(N)]
dp[0][0] = map_data[0][0]

for i in range(N):
    for j in range(M):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + map_data[i][j])
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + map_data[i][j])

if dp[N-1][M-1] <= H:
    print("YES")
    print(dp[N-1][M-1])
else:
    print("NO")
