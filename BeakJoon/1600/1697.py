N, K = map(int, input().split())
visited = [0] * 100001

queue = [N]
while queue:
    x = queue.pop(0)
    if x == K:
        print(visited[x])
        break

    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = visited[x] + 1
            queue.append(nx)
