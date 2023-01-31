#include <stdio.h>

int n, k;
int arr[1001][4];
int memo[101][100001];

int max(int a, int b) { return a > b ? a : b; }

int f(int x, int t, int m) {
    if (t > k || memo[x][t] == -1) return -1;
    if (x == n) return m;
    if (memo[x][t]) return memo[x][t] + m;

    int result = max(f(x + 1, t + arr[x + 1][0], m + arr[x + 1][1]),
                     f(x + 1, t + arr[x + 1][2], m + arr[x + 1][3]));

    if (result == -1)
        memo[x][t] = -1;
    else
        memo[x][t] = result - m;

    return result;
}

int main() {
    scanf("%d %d", &n, &k);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < 4; j++) scanf("%d ", &arr[i][j]);

    printf("%d", max(f(0, arr[0][0], arr[0][1]), f(0, arr[0][2], arr[0][3])));
    return 0;
}
