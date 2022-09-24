#include <stdio.h>

int dp[31][31];

int comb(int n, int r) {
    if (r == 0 || n == r) return 1;
    if (dp[n][r] != 0) return dp[n][r];
    return dp[n][r] = comb(n - 1, r - 1) + comb(n - 1, r);
}

int main(void) {
    int T;
    scanf("%d", &T);

    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        printf("%d\n", comb(m, n));
    }
    return 0;
}