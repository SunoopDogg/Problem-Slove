N = int(input())

count = 0
for i in range(1, N+1):
    while i % 5 == 0:
        count += 1
        i //= 5

print(count)
