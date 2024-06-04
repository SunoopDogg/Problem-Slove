import sys

s = sys.stdin.readline().strip()
code = sys.stdin.readline().strip()

result = 0

hash_map = {}
for index, item in enumerate(s):
    if item not in hash_map:
        hash_map[item] = index + 1
size = len(hash_map)

for i in range(len(code)):
    result *= size
    result += hash_map[code[i]]
    result %= 900528

print(result)