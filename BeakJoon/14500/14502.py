import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
space = []
virus = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            space.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))


def bfs():
    global virus
    visited = [[False] * M for _ in range(N)]
    q = deque(virus)
    cnt = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                arr[nx][ny] = 2
                q.append((nx, ny))
                cnt += 1

    return cnt


max_safe = 0

for walls in combinations(space, 3):
    temp = [row[:] for row in arr]

    for x, y in walls:
        arr[x][y] = 1

    spread = bfs()
    max_safe = max(max_safe, len(space) - spread - 3)

    arr = temp

print(max_safe)
