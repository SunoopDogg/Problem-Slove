import sys

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

INF = float('inf')
dp = {}

def TSP(cur, visited):
    if visited == (1 << N) - 1:
        if W[cur][0]:
            return W[cur][0]
        else:
            return INF

    if (cur, visited) in dp:
        return dp[(cur, visited)]
    
    dp[(cur, visited)] = INF

    for i in range(N):
        if visited & (1 << i) == 0 and W[cur][i]:
            dp[(cur, visited)] = min(dp[(cur, visited)], TSP(i, visited | (1 << i)) + W[cur][i])

    return dp[(cur, visited)]

print(TSP(0, 1 << 0))