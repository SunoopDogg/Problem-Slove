import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
max_cnt = 0
for i in range(N):
    if arr[i] == 0:
        cnt = max(cnt, max_cnt)
        max_cnt = 0
    else:
        max_cnt += 1
cnt = max(cnt, max_cnt)

print(cnt)
