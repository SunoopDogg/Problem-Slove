#include <stdio.h>

int main() {
    int arr[101][101] = {0};
    int cnt = 0;

    for (int i = 0; i < 4; i++) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        for (int j = a; j < c; j++)
            for (int k = b; k < d; k++) arr[j][k] = 1;
    }
    for (int i = 0; i < 100; i++)
        for (int j = 0; j < 100; j++) cnt += arr[i][j];

    printf("%d", cnt);
    return 0;
}