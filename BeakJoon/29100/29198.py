import sys

N, M, K = map(int, sys.stdin.readline().split())
strings = [sys.stdin.readline().rstrip() for _ in range(N)]

if len(set(strings)) == 1:
    combined_str = strings[0] * K
    print("".join(sorted(combined_str)))
    exit()

if M == 1:
    print("".join(sorted(strings)[:K]))
    exit()

sorted_strings = list(map(lambda x: ''.join(sorted(x)), strings))
sorted_strings.sort()
result = ""
for i in range(K):
    result += sorted_strings[i]
print(''.join(sorted(result)))
