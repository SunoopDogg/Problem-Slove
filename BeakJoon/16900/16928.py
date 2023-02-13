import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [0] * 101
for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = y


def bfs():
    q = deque()
    q.append(1)
    visited = [0] * 101
    visited[1] = 1
    while q:
        x = q.popleft()
        if x == 100:
            return visited[x] - 1
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            if board[nx] != 0:
                nx = board[nx]
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)


print(bfs())
