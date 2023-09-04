import sys
import heapq
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
players = defaultdict(list)

for _ in range(N):
    P, W = map(int, sys.stdin.readline().split())
    heapq.heappush(players[P], -W)

for _ in range(K):
    for pos in players:
        if players[pos]:
            top_player_value = -heapq.heappop(players[pos])
            heapq.heappush(players[pos], -max(0, top_player_value - 1))

total_value = sum([-heapq.heappop(players[pos])
                  for pos in players if players[pos]])
print(total_value)
