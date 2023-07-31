import sys

N = int(sys.stdin.readline())

s = int((N+1)*(N+2)/2 - 1)
arr = [i for i in range(2, N+2)]

while True:
    d = set()
    for i in range(2, int(s**0.5)+1):
        if s % i == 0:
            d.add(i)
            d.add(s//i)
    d.add(s)

    if len(set(arr) & d) == 1:
        break
    else:
        s += 1
        arr[-1] += 1

print(*arr)
