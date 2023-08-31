import sys


def prime_list(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


MAX = 4000000

N = int(sys.stdin.readline())
prime = prime_list(MAX)

start = end = sum = cnt = 0
while True:
    if sum >= N:
        sum -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        sum += prime[end]
        end += 1

    if sum == N:
        cnt += 1

print(cnt)
