K = int(input())

stk = []

for _ in range(K):
    x = int(input())
    if x == 0:
        stk.pop()
    else:
        stk.append(x)

print(sum(stk))
