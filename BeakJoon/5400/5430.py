T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()

    arr = arr[1:-1].split(',')
    if n == 0:
        arr = []

    flag = True
    for i in p:
        if i == 'R':
            flag = not flag
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                break

            if flag:
                arr.pop(0)
            else:
                arr.pop()
    else:
        if flag:
            print('[' + ','.join(arr) + ']')
        else:
            print('[' + ','.join(arr[::-1]) + ']')
