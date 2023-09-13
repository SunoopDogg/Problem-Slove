import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = list(sys.stdin.readline().split())

visited = set("".join(A))
target = sorted(A)
answer = -1

q = deque([[A, 0]])
while q:
    s, cnt = q.popleft()
    if s == target:
        answer = cnt
        break
    for i in range(N - K + 1):
        temp = s[i: i + K]
        temp.reverse()
        new_s = s[:i] + temp + s[i + K:]
        if "".join(new_s) not in visited:
            visited.add("".join(new_s))
            q.append([new_s, cnt + 1])

print(answer)
