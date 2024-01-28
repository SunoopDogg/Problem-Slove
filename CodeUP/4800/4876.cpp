#include <stdio.h>

int main() {
    int n;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int a[5] = { 0, }, b[5] = { 0, };
        int m, t;
        scanf("%d", &m);
        for (int j = 0; j < m; j++) {
            scanf("%d", &t);
            a[t]++;
        }
        scanf("%d", &m);
        for (int j = 0; j < m; j++) {
            scanf("%d", &t);
            b[t]++;
        }
        for (int j = 4; j >= 0; j--)
            if (!j) printf("D\n");
            else if (a[j] != b[j]) {
                printf("%c\n", a[j] > b[j] ? 'A' : 'B');
                break;
            }
    }

    return 0;
}