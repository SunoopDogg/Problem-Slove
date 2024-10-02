import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))

result = []

while True:
    max_num = 0

    sorted_A = sorted(set(A))
    sorted_B = sorted(set(B))
    sorted_A.reverse()

    for i in sorted_A:
        if i in sorted_B:
            max_num = i
            break

    if max_num == 0:
        break

    result.append(max_num)

    A = A[A.index(max_num)+1:]
    B = B[B.index(max_num)+1:]

print(len(result))
print(' '.join(map(str, result)))
