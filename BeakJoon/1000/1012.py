import sys
sys.setrecursionlimit(10000)

N, M = 0, 0
arr, visited = [], []


def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return 0
    if visited[x][y] == 1:
        return 0

    visited[x][y] = 1

    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return 1
    return 0


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    for j in range(K):
        X, Y = map(int, input().split())
        arr[X][Y] = 1

    cnt = 0
    for x in range(M):
        for y in range(N):
            cnt += dfs(x, y)

    print(cnt)
