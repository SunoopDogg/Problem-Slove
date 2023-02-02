import sys
N = int(sys.stdin.readline())

time = []
for i in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for i in time:
    if i[0] >= end:
        cnt += 1
        end = i[1]

print(cnt)
