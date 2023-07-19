from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[x][y][1] = 1

    while queue:
        x, y, w = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if graph[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx, ny, w))

    return -1


print(bfs(0, 0))
