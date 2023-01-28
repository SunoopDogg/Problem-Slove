import sys

N, M = map(int, input().split())

dic1 = {}
dic2 = {}
for i in range(N):
    dic1[i+1] = sys.stdin.readline().strip()
    dic2[dic1[i+1]] = i+1

for i in range(M):
    temp = sys.stdin.readline().strip()
    try:
        print(dic1[int(temp)])
    except:
        print(dic2[temp])
