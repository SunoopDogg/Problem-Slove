X = int(input())

pice = [64, 32, 16, 8, 4, 2, 1]

count = 0
for i in pice:
    if X >= i:
        count += X // i
        X %= i

print(count)
