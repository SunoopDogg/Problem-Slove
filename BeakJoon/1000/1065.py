N = int(input())

if N < 100:
    print(N)
else:
    count = 99
    for i in range(100, N+1):
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            count += 1
    print(count)
