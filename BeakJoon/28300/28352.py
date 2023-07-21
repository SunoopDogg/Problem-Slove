import sys

N = int(sys.stdin.readline())


def factorial(n):
    if n == 10:
        return 6

    return n * factorial(n-1)


print(factorial(N))
