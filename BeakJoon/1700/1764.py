N, M = map(int, input().split())

not_heard = set()
for _ in range(N):
    not_heard.add(input())

not_seen = set()
for _ in range(M):
    not_seen.add(input())

result = not_heard & not_seen

print(len(result))
for name in sorted(result):
    print(name)
