import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
problems = [[] for _ in range(5)]

for _ in range(N):
    K, T = map(int, sys.stdin.readline().split())
    problems[K-1].append(T)

for i in range(5):
    problems[i].sort()

total_time = 0
prev_time = 0
prev_difficulty = 0

for i in range(5):
    for j in range(P[i]):
        total_time += problems[i][j]
        if prev_difficulty != i+1 and j == 0:
            total_time += 60
        elif prev_difficulty == i+1:
            total_time += abs(prev_time - problems[i][j])
        prev_time = problems[i][j]
        prev_difficulty = i+1

print(total_time-60)
