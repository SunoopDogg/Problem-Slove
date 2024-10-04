import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

sorted_M = sorted(M)

min_val = 3000000001
result = [1000000000, 1000000000, 1000000000]

for k in range(N):
    i = k+1
    j = N-1
    while i < j:
        sum_val = sorted_M[k]+sorted_M[i]+sorted_M[j]

        if abs(sum_val) < min_val:
            min_val = abs(sum_val)
            result = [sorted_M[k], sorted_M[i], sorted_M[j]]

        if sum_val < 0:
            i += 1
        else:
            j -= 1

print(*result)
