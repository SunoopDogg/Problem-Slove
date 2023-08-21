import sys

R, C, T = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def spread():
    dust = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                dust.append((i, j, room[i][j]))
    for x, y, z in dust:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < R and ny >= 0 and ny < C and room[nx][ny] != -1:
                cnt += 1
                room[nx][ny] += z // 5
        room[x][y] -= (z // 5) * cnt


def clean():
    up = cleaner[0]
    down = cleaner[1]
    for i in range(up - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for i in range(C - 1):
        room[0][i] = room[0][i + 1]
    for i in range(up):
        room[i][C - 1] = room[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        room[up][i] = room[up][i - 1]
    room[up][1] = 0

    for i in range(down + 1, R - 1):
        room[i][0] = room[i + 1][0]
    for i in range(C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    for i in range(R - 1, down, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        room[down][i] = room[down][i - 1]
    room[down][1] = 0


cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

for _ in range(T):
    spread()
    clean()

result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            result += room[i][j]
print(result)
