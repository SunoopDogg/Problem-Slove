#include <stdio.h>

int main() {
    int T;

    scanf("%d", &T);

    while (T--) {
        int x1, y1, r1, x2, y2, r2;

        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

        if (x1 == x2 && y1 == y2 && r1 == r2) {
            printf("-1\n");
            continue;
        }

        int d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
        int sum_r = r1 + r2;
        int dif_r = r1 - r2;

        if (sum_r * sum_r < d || dif_r * dif_r > d)
            printf("0\n");
        else if (sum_r * sum_r == d || dif_r * dif_r == d)
            printf("1\n");
        else
            printf("2\n");
    }

    return 0;
}