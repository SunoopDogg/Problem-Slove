#include <stdio.h>

long long arr[91] = {0, 1};

long long dp(int n) {
    if (arr[n]) return arr[n];
    if (n == 0) return 0;
    return arr[n] = dp(n - 1) + dp(n - 2);
}

int main(void) {
    int n;
    scanf("%d", &n);

    printf("%lld", dp(n));

    return 0;
}