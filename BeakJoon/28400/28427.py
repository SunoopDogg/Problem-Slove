import sys


def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sieve


max_value = 500001
primes = sieve_of_eratosthenes(2*max_value + 1)

arr = [0] * max_value
arr[0] = 1 if primes[1] else 0
for x in range(1, max_value):
    arr[x] = arr[x - 1] + (1 if primes[2*x + 1] else 0)

Q = int(sys.stdin.readline())
for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    print(arr[R - 1] - arr[L - 1])
