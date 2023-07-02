import sys
from collections import deque


def my_round(n):
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)


n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    difficulty = [int(sys.stdin.readline()) for _ in range(n)]
    deq = deque(sorted(difficulty))

    count = my_round(n * 0.15)
    if count != 0:
        for _ in range(count):
            deq.popleft()
            deq.pop()

    print(my_round(sum(deq) / len(deq)))
