N = int(input())
l = list(map(int, input().split()))

size = max(l)

prime = [True] * (size+1)
prime[0] = False
prime[1] = False
for i in range(2, int(size**0.5)+1):
    if prime[i]:
        for j in range(i+i, size+1, i):
            prime[j] = False

print(sum(prime[i] for i in l))
