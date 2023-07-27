import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())


def find_sister(N, K):
    MAX = 100001
    visited = [0]*MAX
    queue = deque([N])
    visited[N] = 1
    while queue:
        v = queue.popleft()
        if v == K:
            return visited[v] - 1
        for next_step in (v-1, v+1, v*2):
            if (0 <= next_step < MAX) and not visited[next_step]:
                if next_step == v*2 and v < K:
                    queue.appendleft(next_step)
                    visited[next_step] = visited[v]
                else:
                    queue.append(next_step)
                    visited[next_step] = visited[v] + 1


print(find_sister(N, K))
