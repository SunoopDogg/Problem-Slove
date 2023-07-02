from collections import deque

n, m = map(int, input().split())
x, y = 0, 0

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            graph[x][y] = 0
        elif graph[i][j] == 1:
            graph[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
queue.append((x, y))

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == -1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

for i in graph:
    print(*i)
