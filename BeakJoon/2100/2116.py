def side_dice(dice, bottom_index, top_index):
    result = []

    for i in range(6):
        if i != bottom_index and i != top_index:
            result.append(dice[i])

    return result


N = int(input())

l = []
for i in range(N):
    l.append(list(map(int, input().split())))

opposite = [5, 3, 4, 1, 2, 0]

max_sum = 0
for i in range(6):
    bottom = l[0][i]
    top = l[0][opposite[i]]

    s = max(side_dice(l[0], i, opposite[i]))
    for j in range(1, N):
        bottom = l[j].index(top)
        top = l[j][opposite[bottom]]

        s += max(side_dice(l[j], bottom, opposite[bottom]))

    max_sum = max(max_sum, s)

print(max_sum)
