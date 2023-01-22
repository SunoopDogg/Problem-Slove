N, K = map(int, input().split())

array = [i for i in range(1, N+1)]

result = []
index = 0

while len(array) > 0:
    index = (index + K - 1) % len(array)
    result.append(str(array.pop(index)))

print("<", ", ".join(result), ">", sep="")
