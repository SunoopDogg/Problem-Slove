#include <stdio.h>

int arr[15][15];

int f(int x, int y) {
    if (arr[x][y]) return arr[x][y];
    return arr[x][y] = f(x, y - 1) + f(x - 1, y);
}

int main(void) {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < 15; i++) {
        arr[0][i] = i + 1;
        arr[i][0] = 1;
    }

    while (T--) {
        int k, n;
        scanf("%d %d", &k, &n);
        printf("%d\n", f(k, n - 1));
    }

    return 0;
}