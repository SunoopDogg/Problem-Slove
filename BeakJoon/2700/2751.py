import sys
N = int(sys.stdin.readline().strip())

l = []
for i in range(N):
    l.append(int(sys.stdin.readline().strip()))

l.sort()

for i in range(N):
    print(l[i])
