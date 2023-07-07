import sys

N, M = map(int, sys.stdin.readline().split())
know = list(map(int, sys.stdin.readline().split()))[1:]

if len(know) == 0:
    print(M)
else:
    party = []
    for _ in range(M):
        party.append(list(map(int, sys.stdin.readline().split()))[1:])

    for _ in range(M):
        for i in range(M):
            for j in range(len(party[i])):
                if party[i][j] in know:
                    know += party[i]
                    know = list(set(know))
                    break

    answer = 0
    for i in range(M):
        if not set(party[i]) & set(know):
            answer += 1

    print(answer)
