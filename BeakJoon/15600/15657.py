import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


def dfs(depth, start, result):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(start, N):
        dfs(depth+1, i, result+[arr[i]])


dfs(0, 0, [])
