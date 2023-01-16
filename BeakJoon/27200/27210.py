N = int(input())
l = map(int, input().split())

left_max, right_max = 0, 0
result = 0

for i in l:
    if i == 1:
        left_max += 1
    else:
        left_max -= 1
    if i == 2:
        right_max += 1
    else:
        right_max -= 1

    if left_max < 0:
        left_max = 0
    if right_max < 0:
        right_max = 0

    if result < left_max + right_max:
        result = left_max + right_max

print(result)
