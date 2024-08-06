import sys

N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))

set_cards = set(cards)

lose_cnt = [0] * 1000001
win_cnt = [0] * 1000001

for i in set_cards:
    for j in range(i+i, 1000001, i):
        lose_cnt[j] += 1
        if j in set_cards:
            win_cnt[i] += 1

for i in cards:
    print(win_cnt[i] - lose_cnt[i], end=' ')
