import sys


def eratos(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [i for i in range(2, n + 1) if prime[i]]


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

prime_nums = eratos(max(arr))
answer = 1
count = 0

for num in prime_nums:
    pow_cnt = []

    for a in arr:
        cnt = 0
        while a % num == 0:
            a //= num
            cnt += 1
        pow_cnt.append(cnt)

    avg = sum(pow_cnt) // N
    answer *= num ** avg

    for i in pow_cnt:
        count += avg - i if avg > i else 0

print(answer, count)
