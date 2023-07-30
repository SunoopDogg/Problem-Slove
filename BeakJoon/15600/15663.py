import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
check = [False] * N
result = set()


def dfs(cnt, arr):
    if cnt == M:
        result.add(tuple(arr))
        return

    for i in range(N):
        if not check[i]:
            check[i] = True
            dfs(cnt + 1, arr + [num[i]])
            check[i] = False


dfs(0, [])
for i in sorted(result):
    print(*i)
