N, K = map(int, input().split())


def binomial_coefficient(n, k):
    if n == k or k == 0:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)


print(binomial_coefficient(N, K))
