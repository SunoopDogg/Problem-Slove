memo = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}


def padovan(n):
    if n in memo:
        return memo[n]

    memo[n] = padovan(n - 1) + padovan(n - 5)
    return memo[n]


T = int(input())

for _ in range(T):
    N = int(input())

    print(padovan(N))
