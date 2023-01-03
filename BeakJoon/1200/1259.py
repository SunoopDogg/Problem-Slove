while True:
    s = input()

    if s == "0":
        break

    result = 0
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            result = 1
            break

    if result == 0:
        print("yes")
    else:
        print("no")
