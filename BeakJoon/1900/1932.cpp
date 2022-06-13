#include <stdio.h>

int max(int a, int b) { return a > b ? a : b; }

int main(void) {
    int n;
    int arr[505][505];

    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= i; j++) scanf("%d", &arr[i][j]);

    for (int i = n - 1; i >= 1; i--)
        for (int j = 1; j <= i; j++)
            arr[i][j] += max(arr[i + 1][j], arr[i + 1][j + 1]);

    printf("%d\n", arr[1][1]);

    return 0;
}