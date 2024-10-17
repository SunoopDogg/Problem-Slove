import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
R, C, D = map(int, sys.stdin.readline().split())

room = [[] for _ in range(N)]
for i in range(N):
    room[i] = list(map(int, sys.stdin.readline().split()))

result = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r, c, d):
    global result
    if room[r][c] == 0:
        room[r][c] = 2
        result += 1

    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]
        if room[nr][nc] == 0:
            clean(nr, nc, d)
            return

    if room[r - dr[d]][c - dc[d]] == 1:
        return

    clean(r - dr[d], c - dc[d], d)


clean(R, C, D)
print(result)
