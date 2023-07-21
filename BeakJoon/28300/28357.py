import sys

N, K = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))


def count_candies(scores, X):
    candies = 0
    for score in scores:
        if score > X:
            candies += (score - X)
    return candies


def find_min_X(scores, K):
    left = 0
    right = max(scores)
    while left <= right:
        mid = (left + right) // 2
        if count_candies(scores, mid) > K:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(find_min_X(score, K))
