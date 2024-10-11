import sys
sys.setrecursionlimit(10**6)


def dfs(n):
    global count

    visited[n] = True
    cycle_list.append(n)

    if visited[A[n]] == True:
        if A[n] in cycle_list:
            count -= len(cycle_list[cycle_list.index(A[n]):])
        return
    else:
        dfs(A[n])


T = int(sys.stdin.readline())


while T:
    T -= 1
    N = int(sys.stdin.readline())
    A = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (N + 1)
    count = N
    for i in range(1, N + 1):
        if not visited[i]:
            cycle_list = []
            dfs(i)

    print(count)
