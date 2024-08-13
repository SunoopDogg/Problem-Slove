import sys

N = int(sys.stdin.readline().strip())
fruit = list(map(int, sys.stdin.readline().strip().split()))

if (len(set(fruit)) <= 2):
    print(len(fruit))
    exit()

result = 1

start_index = 0
end_index = 1
target = {fruit[start_index], fruit[end_index]}

while (end_index != len(fruit) - 1):
    end_index += 1

    if fruit[end_index] not in target:
        if (len(target) < 2):
            target.add(fruit[end_index])
            continue

        start_index = end_index - 1
        target = {fruit[start_index], fruit[end_index]}
        while (len(target) != 3):
            start_index -= 1
            target.add(fruit[start_index])
        target.remove(fruit[start_index])
        start_index += 1

    if (result < end_index - start_index):
        result = end_index - start_index

print(result + 1)
