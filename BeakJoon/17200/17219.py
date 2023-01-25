import sys

N, M = map(int, sys.stdin.readline().split())

dic = {}
for i in range(N):
    site, password = sys.stdin.readline().split()
    dic[site] = password

for i in range(M):
    site = sys.stdin.readline().split()
    print(dic[site[0]])
