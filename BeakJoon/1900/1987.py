import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

answer = 0
visited = set()

visited.add((0, 0, board[0][0]))
q = deque([(0, 0, board[0][0], 1)])

while q:
    r, c, path, cnt = q.popleft()
    answer = max(answer, cnt)
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in path:
            if (nr, nc, path + board[nr][nc]) not in visited:
                visited.add((nr, nc, path + board[nr][nc]))
                q.append((nr, nc, path + board[nr][nc], cnt + 1))

print(answer)
