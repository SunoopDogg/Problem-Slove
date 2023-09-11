def cal(x, y):
    return (x//3)*3 + (y//3)


def sol(n):
    if n == 81:
        for a in A:
            print(''.join(list(map(str, a))))
        return True

    x = n // 9
    y = n % 9

    if A[x][y]:
        return sol(n+1)
    else:
        for i in range(1, 10):
            if not c1[x][i] and not c2[y][i] and not c3[cal(x, y)][i]:
                c1[x][i] = c2[y][i] = c3[cal(x, y)][i] = True
                A[x][y] = i
                if sol(n+1):
                    return True
                c1[x][i] = c2[y][i] = c3[cal(x, y)][i] = False
                A[x][y] = 0

    return False


A = [list(map(int, input())) for _ in range(9)]
c1 = [[False]*10 for _ in range(9)]
c2 = [[False]*10 for _ in range(9)]
c3 = [[False]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if A[i][j]:
            c1[i][A[i][j]] = True
            c2[j][A[i][j]] = True
            c3[cal(i, j)][A[i][j]] = True
sol(0)
