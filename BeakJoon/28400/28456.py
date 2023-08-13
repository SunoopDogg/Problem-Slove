import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = int(sys.stdin.readline())

for _ in range(Q):
    op = list(map(int, sys.stdin.readline().split()))

    if op[0] == 1:
        arr[op[1]-1].insert(0, arr[op[1]-1].pop())
    else:
        A = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                A[j][N-i-1] = arr[i][j]
        arr = A

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
