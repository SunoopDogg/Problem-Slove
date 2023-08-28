import sys
from bisect import bisect_left, bisect_right


def find_combinations(array, target_sum):
    result = 0
    length = len(array)
    left = array[:length//2]
    right = array[length//2:]

    left_sum = []
    right_sum = []

    for i in range(1 << len(left)):
        temp_sum = 0
        for j in range(len(left)):
            if i & (1 << j):
                temp_sum += left[j]
        left_sum.append(temp_sum)

    for i in range(1 << len(right)):
        temp_sum = 0
        for j in range(len(right)):
            if i & (1 << j):
                temp_sum += right[j]
        right_sum.append(temp_sum)

    left_sum.sort()

    for r in right_sum:
        result += bisect_right(left_sum, target_sum - r) - \
            bisect_left(left_sum, target_sum - r)

    if target_sum == 0:
        result -= 1

    return result


N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

print(find_combinations(numbers, S))
