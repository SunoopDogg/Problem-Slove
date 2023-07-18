import sys

N = int(sys.stdin.readline())
first = list(map(int, sys.stdin.readline().split()))

dp_max = first
dp_min = first
for _ in range(N-1):
    num = list(map(int, sys.stdin.readline().split()))

    dp_max = [max(dp_max[0], dp_max[1]) + num[0], max(dp_max) +
              num[1], max(dp_max[1], dp_max[2]) + num[2]]
    dp_min = [min(dp_min[0], dp_min[1]) + num[0], min(dp_min) +
              num[1], min(dp_min[1], dp_min[2]) + num[2]]

print(max(dp_max), min(dp_min))
