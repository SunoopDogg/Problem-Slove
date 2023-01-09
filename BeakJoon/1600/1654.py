K, N = map(int, input().split())

num = []
for _ in range(K):
    num.append(int(input()))

start = 1
end = max(num)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in num:
        total += i // mid

    if total >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
