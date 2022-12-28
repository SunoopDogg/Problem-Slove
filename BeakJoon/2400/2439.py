N = int(input())

for i in range(N):
    for j in range(N):
        if j + 1 >= N - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
