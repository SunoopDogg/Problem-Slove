import sys

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def mul(A, B):
    C = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C


def div(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif B % 2 == 0:
        return div(mul(A, A), B // 2)
    else:
        return mul(div(mul(A, A), B // 2), A)


for i in div(A, B):
    print(*i)
