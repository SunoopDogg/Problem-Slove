import sys

MOD = 10**9

N = int(sys.stdin.readline())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for length in range(2, N + 1):
    for last_digit in range(10):
        for used_digits in range(1 << 10):
            if last_digit == 0:
                dp[length][0][used_digits | (
                    1 << 0)] += dp[length-1][1][used_digits]
            elif last_digit == 9:
                dp[length][9][used_digits | (
                    1 << 9)] += dp[length-1][8][used_digits]
            else:
                dp[length][last_digit][used_digits | (
                    1 << last_digit)] += dp[length-1][last_digit-1][used_digits]
                dp[length][last_digit][used_digits | (
                    1 << last_digit)] += dp[length-1][last_digit+1][used_digits]

            dp[length][last_digit][used_digits | (1 << last_digit)] %= MOD

answer = 0
for i in range(10):
    answer += dp[N][i][(1 << 10) - 1]
    answer %= MOD

print(answer)
