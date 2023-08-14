import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()


def solution(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


if A.isdigit():
    print(solution(int(A)+3))
elif B.isdigit():
    print(solution(int(B)+2))
elif C.isdigit():
    print(solution(int(C)+1))
