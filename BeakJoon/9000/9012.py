T = int(input())

for i in range(T):
    s = input()

    cnt = 0
    for j in s:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break

    if cnt == 0:
        print("YES")
    else:
        print("NO")
