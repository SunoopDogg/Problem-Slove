import sys
import queue

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def find_air():
    q = queue.Queue()
    q.put((0, 0))

    q1 = queue.Queue()
    out_air = [[False] * M for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while not q.empty():
        x, y = q.get()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    q.put((nx, ny))
                    out_air[nx][ny] = True
                elif board[nx][ny] == 1:
                    q1.put((nx, ny))

    while not q1.empty():
        cnt = 0
        x, y = q1.get()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and out_air[nx][ny]:
                cnt += 1

        if cnt >= 2:
            board[x][y] = 2


def melt_cheese():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                board[i][j] = 0


def check_cheese():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                return True
    return False


time = 0
while True:
    find_air()
    if not check_cheese():
        break
    melt_cheese()
    time += 1

print(time + 1)
