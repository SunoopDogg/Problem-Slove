import sys

N, M = map(int, sys.stdin.readline().split())


def count_plants_corrected(N, M, experiments):
    plants = {i: {"P": None, "M": None} for i in range(1, N + 1)}

    for exp in experiments:
        a, b, c = exp
        plants[a][b] = c

    min_plants = 0
    max_plants = 0

    for plant in plants.values():
        if plant["P"] == 1 and plant["M"] == 0:
            min_plants += 1
            max_plants += 1
        elif plant["P"] == 1 and plant["M"] is None:
            max_plants += 1
        elif plant["P"] is None and plant["M"] in [0, None]:
            max_plants += 1

    return min_plants, max_plants


experiments = []
for _ in range(M):
    a, b, c = sys.stdin.readline().split()
    experiments.append((int(a), b, int(c)))

min_plants, max_plants = count_plants_corrected(N, M, experiments)
print(min_plants, max_plants)
