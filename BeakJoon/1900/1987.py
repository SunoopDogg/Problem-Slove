import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
visited = set()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(board[nx][ny])


visited.add(board[0][0])
dfs(0, 0, 1)
print(ans)
