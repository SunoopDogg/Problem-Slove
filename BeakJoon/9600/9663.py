import sys


N = int(sys.stdin.readline().strip())


rows = [0] * N
neg_diagonals = [0] * (2*N - 1)
pos_diagonals = [0] * (2*N - 1)


def place_queens(n, row, rows, neg_diagonals, pos_diagonals):
    if row == n:
        return 1
    count = 0
    for i in range(n):
        if not rows[i] and not neg_diagonals[row-i+n-1] and not pos_diagonals[row+i]:
            rows[i] = neg_diagonals[row-i+n-1] = pos_diagonals[row+i] = 1
            count += place_queens(n, row+1, rows, neg_diagonals, pos_diagonals)
            rows[i] = neg_diagonals[row-i+n-1] = pos_diagonals[row+i] = 0
    return count


print(place_queens(N, 0, rows, neg_diagonals, pos_diagonals))
