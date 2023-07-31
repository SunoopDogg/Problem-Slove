import sys

N = int(sys.stdin.readline())


base = [
    "  *  ",
    " * * ",
    "*****"
]
board = ["" for _ in range(N*3)]


def make_star(n):
    if n == 3:
        board[0] = base[0]
        board[1] = base[1]
        board[2] = base[2]
        return

    make_star(n//2)
    for i in range(n//2):
        board[n//2 + i] = board[i] + " " + board[i]
    for i in range(n//2):
        board[i] = " " * (n//2) + board[i] + " " * (n//2)


make_star(N)
for i in range(N):
    print(board[i])
