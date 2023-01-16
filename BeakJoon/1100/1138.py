N = int(input())
l = list(map(int, input().split()))

result = [0] * N
for i in range(N):
    count = 0
    for j in range(N):
        if count == l[i] and result[j] == 0:
            result[j] = i+1
            break
        if result[j] == 0:
            count += 1

print(*result)
