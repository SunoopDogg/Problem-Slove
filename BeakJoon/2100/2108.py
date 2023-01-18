import sys

N = int(sys.stdin.readline())

l = [0] * 8001

for i in range(N):
    l[int(sys.stdin.readline()) + 4000] += 1

new_l = []
max_l = []
max_cnt = max(l)
for i in range(8001):
    if l[i] != 0:
        for j in range(l[i]):
            new_l.append(i - 4000)
        if l[i] == max_cnt:
            max_l.append(i - 4000)

print(round(sum(new_l) / N))
print(new_l[N // 2])
if len(max_l) == 1:
    print(max_l[0])
else:
    print(max_l[1])
print(new_l[-1] - new_l[0])
