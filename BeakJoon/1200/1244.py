n = int(input())
l = list(map(bool, map(int, input().split())))
m = int(input())

for i in range(m):
    g, s = map(int, input().split())
    if g == 1:
        for j in range(s-1, n, s):
            l[j] = not l[j]
    else:
        for j in range(1, min(s, n-s+1)):
            if l[s-1-j] == l[s-1+j]:
                l[s-1-j] = not l[s-1-j]
                l[s-1+j] = not l[s-1+j]
            else:
                break
        l[s-1] = not l[s-1]

for i in range(n):
    if l[i]:
        print(1, end=' ')
    else:
        print(0, end=' ')
    if (i % 20 == 19):
        print()
