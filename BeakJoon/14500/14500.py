import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


visited = [[False] * M for _ in range(N)]


def dfs(x, y, cnt, sum):
    global result

    if cnt == 4:
        result = max(result, sum)
        return

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, sum + board[nx][ny])
            visited[nx][ny] = False


ex = [[0, 0, 0, 1], [0, 1, 2, 1], [0, 0, 0, -1], [0, -1, 0, 1]]
ey = [[0, 1, 2, 1], [0, 0, 0, 1],  [0, 1, 2, 1], [0, 1, 1, 1]]


def exception(x, y):
    global result

    for i in range(4):
        sum = 0

        for j in range(4):
            nx = x + ex[i][j]
            ny = y + ey[i][j]

            if 0 <= nx < N and 0 <= ny < M:
                sum += board[nx][ny]
            else:
                break

        result = max(result, sum)


result = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        exception(i, j)

print(result)
