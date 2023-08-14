import sys


M = int(sys.stdin.readline())

ball_dict = {}
for _ in range(M):
    request = list(map(int, sys.stdin.readline().split()))

    if request[0] == 1:
        _, x, w = request
        ball_dict[w] = x

    elif request[0] == 2:
        _, w = request
        print(ball_dict[w])
