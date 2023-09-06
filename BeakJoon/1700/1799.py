import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[False] * (N * 3) for _ in range(2)]


def recur(y, x, cnt):
    global ans

    if N % 2:
        if x == N:
            y += 1
            x = 0
        elif x == N + 1:
            y += 1
            x = 1
    else:
        if x == N:
            y += 1
            x = 1
        elif x == N + 1:
            y += 1
            x = 0

    if y == N:
        if ans < cnt:
            ans = cnt
        return

    if arr[y][x] == 1 and not visited[0][y + x] and not visited[1][y - x]:
        visited[0][y + x] = True
        visited[1][y - x] = True
        recur(y, x + 2, cnt + 1)
        visited[0][y + x] = False
        visited[1][y - x] = False

    recur(y, x + 2, cnt)


ans = 0
recur(0, 0, 0)
black = ans
ans = 0
recur(0, 1, 0)
white = ans
print(black + white)
