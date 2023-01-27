string = input()

minus = string.split('-')
if minus[0] == '':
    minus[0] = '0'
for i in range(len(minus)):
    minus[i] = sum(list(map(int, minus[i].split('+'))))

print(minus[0] - sum(minus[1:]))
