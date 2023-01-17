def d(n):
    return n + sum([int(i) for i in str(n)])


self_num = set(range(1, 10001))
self_num -= set([d(i) for i in range(1, 10001)])
for i in sorted(self_num):
    print(i)
