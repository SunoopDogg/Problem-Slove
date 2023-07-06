import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

arr = []
sx, sy = 0, 0
for i in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))
    for j in range(M):
        if arr[i][j] == 'I':
            sx, sy = i, j

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global cnt

    if x < 0 or x >= N or y < 0 or y >= M or arr[x][y] == 'X':
        return

    if arr[x][y] != 'X':
        if arr[x][y] == 'P':
            cnt += 1
        arr[x][y] = 'X'

        for i in range(4):
            dfs(x + dx[i], y + dy[i])


cnt = 0
dfs(sx, sy)
print("TT" if cnt == 0 else cnt)
