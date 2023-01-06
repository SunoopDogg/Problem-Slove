N = int(input())
A = list(map(int, input().split()))
M = int(input())
l = map(int, input().split())

A.sort()

for i in l:
    flag = 0
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == i:
            print(1)
            flag = 1
            break
        elif A[mid] > i:
            end = mid - 1
        else:
            start = mid + 1

    if flag == 0:
        print(0)
