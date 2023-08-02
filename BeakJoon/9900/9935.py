import sys

input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)
stack = []


for i in string:
    stack.append(i)
    if i == bomb[-1]:
        if ''.join(stack[-bomb_len:]) == bomb:
            del stack[-bomb_len:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
