M = int(input())
N = int(input())

arr = [True] * (N+1)
arr[1] = False

for i in range(2, N+1):
    if arr[i]:
        for j in range(i+i, N+1, i):
            arr[j] = False

arr_sum = 0
arr_min = 0
for i in range(M, N+1):
    if arr[i]:
        arr_sum += i
        if arr_min == 0:
            arr_min = i

if arr_sum == 0:
    print(-1)
else:
    print(arr_sum)
    print(arr_min)
