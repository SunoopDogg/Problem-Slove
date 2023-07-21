import sys

N, M = map(int, sys.stdin.readline().split())


def assign_exams(M, N):
    grid = [[0 for _ in range(M)] for _ in range(N)]

    colors = [1, 2, 3, 4]

    for i in range(N):
        for j in range(M):
            for color in colors:
                if (
                    (i > 0 and grid[i - 1][j] == color) or
                    (j > 0 and grid[i][j - 1] == color) or
                    (i > 0 and j > 0 and grid[i - 1][j - 1] == color) or
                    (i > 0 and j < M - 1 and grid[i - 1][j + 1] == color)
                ):
                    continue

                grid[i][j] = color
                break

    return grid


grid = assign_exams(M, N)
print(len(set(grid[i][j] for i in range(N) for j in range(M))))
for i in range(N):
    print(*grid[i])
