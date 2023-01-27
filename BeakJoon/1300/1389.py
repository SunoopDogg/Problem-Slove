N, M = map(int, input().split())

INF = int(1e9)
distance = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            distance[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            distance[a][b] = min(
                distance[a][b], distance[a][k] + distance[k][b])

result = []
for i in range(1, N + 1):
    result.append(sum(distance[i][1:]))

min_value = min(result)
for i in range(1, N + 1):
    if result[i - 1] == min_value:
        print(i)
        break
