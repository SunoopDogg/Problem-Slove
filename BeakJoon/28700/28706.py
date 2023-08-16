import sys


def calc(op, v1, v2):
    if op == '*':
        return (v1 * v2) % 7
    else:
        return (v1 + v2) % 7


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    D = [[False] * 7 for _ in range(N + 1)]
    D[0][1] = True

    for i in range(1, N + 1):
        op1, v1, op2, v2 = input().split()
        v1, v2 = int(v1), int(v2)
        for x in range(7):
            if D[i - 1][x]:
                D[i][calc(op1, x, v1)] = True
                D[i][calc(op2, x, v2)] = True

    print("LUCKY" if D[N][0] else "UNLUCKY")
