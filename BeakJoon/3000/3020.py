import sys

N, H = map(int, sys.stdin.readline().split())

even_list = [0] * (H + 1)
odd_list = [0] * (H + 1)

for i in range(N):
    if i % 2 == 0:
        even_list[int(sys.stdin.readline())] += 1
    else:
        odd_list[int(sys.stdin.readline())] += 1


for i in range(H - 1, 0, -1):
    even_list[i] += even_list[i + 1]
    odd_list[i] += odd_list[i + 1]

min_break = N
count = 0

for i in range(1, H + 1):
    if min_break > even_list[i] + odd_list[H - i + 1]:
        min_break = even_list[i] + odd_list[H - i + 1]
        count = 1
    elif min_break == even_list[i] + odd_list[H - i + 1]:
        count += 1

print(min_break, count)
