import sys


def postfix(expression):
    stack = []
    result = ''

    for i in expression:
        if i.isalpha():
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*' or i == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(i)
            elif i == '+' or i == '-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()

    while stack:
        result += stack.pop()

    return result


string = sys.stdin.readline().rstrip()
print(postfix(string))
