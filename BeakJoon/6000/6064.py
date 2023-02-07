import sys


def solve(m, n, x, y):
    i = 0
    while True:
        if (m * i + x) % n == y % n:
            return m * i + x
        i += 1
        if m * i + x > m * n:
            return -1


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(solve(M, N, x, y))
