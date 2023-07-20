import sys


def LCS(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    arr = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    return arr[len1][len2]


str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

print(LCS(str1, str2))
