n = int(input())

stack, result = [], []
index = 1

for _ in range(n):
    num = int(input())

    while index <= num:
        stack.append(index)
        result.append('+')
        index += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

for i in result:
    print(i)
