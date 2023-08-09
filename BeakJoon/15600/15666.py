import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(set(arr))


def dfs(depth, N, M):
    if depth == M:
        print(*result)
        return
    for i in range(len(arr)):
        if len(result) > 0 and result[-1] > arr[i]:
            continue
        result.append(arr[i])
        dfs(depth + 1, N, M)
        result.pop()


result = []
dfs(0, N, M)
