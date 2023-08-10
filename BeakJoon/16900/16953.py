import sys

A, B = map(int, sys.stdin.readline().split())


def solution(A, B):
    count = 0
    while True:
        if A == B:
            return count + 1
        elif A > B:
            return -1
        else:
            if B % 2 == 0:
                B //= 2
                count += 1
            else:
                if B % 10 == 1:
                    B //= 10
                    count += 1
                else:
                    return -1


print(solution(A, B))
