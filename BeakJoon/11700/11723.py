import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    temp = sys.stdin.readline().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif temp[0] == 'empty':
            S = set()
    else:
        command, num = temp[0], int(temp[1])

        if command == 'add':
            S.add(num)
        elif command == 'remove':
            S.discard(num)
        elif command == 'check':
            print(1 if num in S else 0)
        elif command == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)
