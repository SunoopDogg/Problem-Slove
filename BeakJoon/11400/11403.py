import sys

N = int(sys.stdin.readline())

G = []
for _ in range(N):
    G.append(list(map(int, sys.stdin.readline().split())))


def find_path(start, end):
    queue = [start]
    visited = []

    while queue:
        node = queue.pop(0)

        for i in range(N):
            if i not in visited and G[node][i] == 1:
                G[start][i] = 1
                visited.append(i)
                queue.append(i)

        if end in visited:
            G[start][end] = 1
            return 1
    return 0


for i in range(N):
    for j in range(N):
        print(find_path(i, j), end=' ')
    print()
