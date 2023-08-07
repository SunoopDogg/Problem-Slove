import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

min_time = 100000
cnt = 0
visited = [False] * 100001

q = deque()
q.append((N, 0))
while q:
    x, time = q.popleft()
    visited[x] = True
    if time > min_time:
        continue
    if x == K:
        if time < min_time:
            min_time = time
            cnt = 1
        elif time == min_time:
            cnt += 1
    if x + 1 <= 100000 and not visited[x + 1]:
        q.append((x + 1, time + 1))
    if x - 1 >= 0 and not visited[x - 1]:
        q.append((x - 1, time + 1))
    if 2 * x <= 100000 and not visited[2 * x]:
        q.append((2 * x, time + 1))

print(min_time)
print(cnt)
