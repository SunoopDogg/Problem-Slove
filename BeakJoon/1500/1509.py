import sys

string = sys.stdin.readline().strip()
dp = [[0 for _ in range(len(string))] for _ in range(len(string))]

for i in range(len(string)):
    dp[i][i] = 1

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, len(string)):
    for j in range(len(string) - i):
        if string[j] == string[j + i] and dp[j + 1][j + i - 1] == 1:
            dp[j][j + i] = 1

dp2 = [0 for _ in range(len(string))]
for i in range(len(string)):
    if dp[0][i] == 1:
        dp2[i] = 0
    else:
        dp2[i] = 1000000000
        for j in range(i):
            if dp[j + 1][i] == 1 and dp2[i] > dp2[j] + 1:
                dp2[i] = dp2[j] + 1

print(dp2[len(string) - 1] + 1)
