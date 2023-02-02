N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = []


def quadtree(x, y, n):
    global ans

    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != check:
                ans.append('(')
                quadtree(x, y, n//2)
                quadtree(x, y+n//2, n//2)
                quadtree(x+n//2, y, n//2)
                quadtree(x+n//2, y+n//2, n//2)
                ans.append(')')
                return

    ans.append(str(check))


quadtree(0, 0, N)
print(''.join(ans))
