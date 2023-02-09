import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


def dfs(x, y, color):
    visited[x][y] = True

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == color and not visited[nx][ny]:
            dfs(nx, ny, color)


def solution():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, graph[i][j])
                cnt += 1
    return cnt


print(solution(), end=' ')

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
print(solution())
