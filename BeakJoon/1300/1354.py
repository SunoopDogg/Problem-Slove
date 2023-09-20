import sys

n, p, q, x, y = map(int, sys.stdin.readline().split())
dp = {0: 1}


def solve(i):
    i = max(i, 0)

    ai = dp.get(i, None)
    if ai:
        return ai

    ap = solve(i // p - x)
    aq = solve(i // q - y)

    dp[i] = ap + aq
    return dp[i]


print(solve(n))
