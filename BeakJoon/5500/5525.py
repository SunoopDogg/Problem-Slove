import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

cnt = 0
i = 0
while i < M - 2:
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':
        j = i + 3
        while j < M - 1 and S[j] == 'O' and S[j + 1] == 'I':
            j += 2
        if (j - i) // 2 >= N:
            cnt += (j - i) // 2 - N + 1
        i = j - 1
    i += 1

print(cnt)
