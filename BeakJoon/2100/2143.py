import sys
import bisect

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

n_sum = []
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += n_arr[j]
        n_sum.append(sum)

m_sum = []
for i in range(M):
    sum = 0
    for j in range(i, M):
        sum += m_arr[j]
        m_sum.append(sum)

n_sum.sort()
m_sum.sort()

answer = 0
for i in range(len(n_sum)):
    l = bisect.bisect_left(m_sum, T - n_sum[i])
    r = bisect.bisect_right(m_sum, T - n_sum[i])
    answer += r - l

print(answer)
