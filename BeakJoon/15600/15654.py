import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = [0] * M
check = [False] * N


def dfs(depth, N, M):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        result[depth] = arr[i]
        dfs(depth + 1, N, M)
        check[i] = False


dfs(0, N, M)
