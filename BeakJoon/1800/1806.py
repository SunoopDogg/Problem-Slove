import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    arr[i] += arr[i - 1]

start, end = 0, 1
answer = 100001
while start < N:
    if arr[end - 1] - (arr[start - 1] if start > 0 else 0) >= S:
        answer = min(answer, end - start)
        start += 1
    else:
        if end < N:
            end += 1
        else:
            start += 1

print(answer if answer != 100001 else 0)
