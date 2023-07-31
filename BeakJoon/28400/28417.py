import sys

N = int(sys.stdin.readline())

max_score = 0
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    score = max(arr[0], arr[1]) + sum(sorted(arr[2:])[3:])
    if score > max_score:
        max_score = score

print(max_score)
