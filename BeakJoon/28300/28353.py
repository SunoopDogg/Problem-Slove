import sys

N, K = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()

cnt = 0
left, right = 0, N - 1
while left < right:
    if weight[left] + weight[right] <= K:
        cnt += 1
        left += 1
        right -= 1

    else:
        right -= 1

print(cnt)
