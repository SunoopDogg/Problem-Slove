s = input()

result = 0.0

if s[0] != 'F':
    if s[0] == 'A':
        result += 4.0
    elif s[0] == 'B':
        result += 3.0
    elif s[0] == 'C':
        result += 2.0
    elif s[0] == 'D':
        result += 1.0

    if s[1] == '+':
        result += 0.3
    elif s[1] == '-':
        result -= 0.3

print(result)
