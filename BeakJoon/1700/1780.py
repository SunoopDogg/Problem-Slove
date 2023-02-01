N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt0 = 0
cnt1 = 0
cnt2 = 0


def check(x, y, n):
    global cnt0, cnt1, cnt2
    check_num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check_num != arr[i][j]:
                for k in range(3):
                    for l in range(3):
                        check(x+k*n//3, y+l*n//3, n//3)
                return
    if check_num == -1:
        cnt0 += 1
    elif check_num == 0:
        cnt1 += 1
    else:
        cnt2 += 1


check(0, 0, N)
print(cnt0)
print(cnt1)
print(cnt2)
