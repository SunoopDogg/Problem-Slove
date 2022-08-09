#include <stdio.h>

int main(void) {
    int T;

    scanf("%d", &T);

    while (T--) {
        int cnt = 0;

        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        int n;
        scanf("%d", &n);

        while (n--) {
            int x, y, r;

            scanf("%d %d %d", &x, &y, &r);

            int d1 = (x - x1) * (x - x1) + (y - y1) * (y - y1);
            int d2 = (x - x2) * (x - x2) + (y - y2) * (y - y2);

            if (d1 <= r * r || d2 <= r * r) cnt++;
            if (d1 <= r * r && d2 <= r * r) cnt--;
        }

        printf("%d\n", cnt);
    }

    return 0;
}