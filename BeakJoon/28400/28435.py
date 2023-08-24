import sys

MOD = 10**9 + 7
N, K = map(int, sys.stdin.readline().split())
c = [0]*K
*A, = map(int, sys.stdin.readline().split())
for a in A:
    c[a % K] += 1

ans = 1
for i in range(1, (K + 1) // 2):
    ans = ans * (pow(2, c[i], MOD) + pow(2, c[K-i], MOD) - 1) % MOD

ans = ans * (c[0] + 1) % MOD
if K % 2 == 0:
    ans = ans * (c[K // 2] + 1) % MOD
ans = (ans - (N + 1)) % MOD
print(ans)
