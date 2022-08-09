#include <stdio.h>

int arr[41] = {0, 1};

int dp(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (arr[n]) return arr[n];
    return arr[n] = dp(n - 1) + dp(n - 2);
}

int main(void) {
    int T;
    scanf("%d", &T);

    while (T--) {
        int N;

        scanf("%d", &N);

        if (N == 0)
            printf("1 0\n");
        else if (N == 1)
            printf("0 1\n");
        else
            printf("%d %d\n", dp(N - 1), dp(N));
    }

    return 0;
}