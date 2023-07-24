import sys

n = int(sys.stdin.readline())


MOD = 1000000007


def matrix_mult(A, B):
    a, b, c = A
    d, e, f = B
    return ((a*d + b*e) % MOD, (a*e + b*f) % MOD, (b*e + c*f) % MOD)


def matrix_power(A, power):
    if power <= 0:
        return (1, 0, 0)
    elif power == 1:
        return A
    else:
        Y = matrix_power(A, power // 2)
        Y_square = matrix_mult(Y, Y)
        if power % 2 == 0:
            return Y_square
        else:
            return matrix_mult(Y_square, A)


def fibonacci(n):
    if n <= 0:
        return 0
    else:
        return matrix_power((1, 1, 0), n-1)[0]


print(fibonacci(n))
