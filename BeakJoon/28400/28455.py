import sys

N = int(sys.stdin.readline())

level = [int(sys.stdin.readline()) for _ in range(N)]
level.sort(reverse=True)

levelSum = 0
power = 0

for i in level[:42]:
    if i >= 250:
        power += 5
    elif i >= 200:
        power += 4
    elif i >= 140:
        power += 3
    elif i >= 100:
        power += 2
    elif i >= 60:
        power += 1

    levelSum += i

print(levelSum, power)
