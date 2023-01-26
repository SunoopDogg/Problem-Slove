import sys
sys.setrecursionlimit(10**6)

N, r, c = map(int, input().split())


def z(n, x, y):
    if n == 1:
        return 0
    n //= 2
    for i in range(2):
        for j in range(2):
            if x < n * (i + 1) and y < n * (j + 1):
                return (i * 2 + j) * n * n + z(n, x - n * i, y - n * j)


print(z(2 ** N, r, c))
