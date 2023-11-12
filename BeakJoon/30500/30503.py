import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())
for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        l, r, k = query[1:]
        print(arr[l - 1:r].count(k))
    else:
        l, r = query[1:]
        for i in range(l - 1, r):
            arr[i] = 0
