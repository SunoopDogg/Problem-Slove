import sys
n, m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        arr[i][j] += arr[i-1][j]

for i in range(n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    if x1 == 0 and y1 == 0:
        print(arr[x2][y2])
    elif x1 == 0:
        print(arr[x2][y2] - arr[x2][y1-1])
    elif y1 == 0:
        print(arr[x2][y2] - arr[x1-1][y2])
    else:
        print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])
