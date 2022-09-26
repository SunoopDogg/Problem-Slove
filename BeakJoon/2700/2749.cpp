#include <stdio.h>

long long arr[1500001] = {0, 1};

long long dp(int n) {
    if (arr[n]) return arr[n];
    if (n == 0) return 0;
    return arr[n] = (dp(n - 1) + dp(n - 2)) % 1000000;
}

int main(void) {
    long long n;
    scanf("%lld", &n);

    printf("%lld", dp(n % 1500000) % 1000000);

    return 0;
}