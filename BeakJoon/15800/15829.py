L = int(input())
string = input()

hash = 0
for i in range(L):
    hash += (ord(string[i]) - ord('a') + 1) * (31 ** i) % 1234567891

print(hash % 1234567891)
