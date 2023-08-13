import sys

currentDate = sys.stdin.readline().split()
N = int(sys.stdin.readline())

cnt = 0
y, m, d = currentDate[0].split('-')

for _ in range(N):
    i = sys.stdin.readline().rstrip()
    ey, em, ed = i.split('-')
    if int(ey) > int(y):
        cnt += 1
    elif int(ey) == int(y):
        if int(em) > int(m):
            cnt += 1
        elif int(em) == int(m):
            if int(ed) >= int(d):
                cnt += 1

print(cnt)
