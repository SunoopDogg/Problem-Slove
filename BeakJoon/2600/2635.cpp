#include <stdio.h>

int main() {
    int n;
    int max = 0;
    int index = 0;

    scanf("%d", &n);

    for (int i = 0; i <= n; i++) {
        int first = n;
        int second = n - i;
        int cnt = 0;

        while (second >= 0) {
            int tmp = first;
            first = second;
            second = tmp - second;
            cnt++;
        }

        if (cnt > max) {
            max = cnt;
            index = i;
        }
    }

    printf("%d\n", max + 1);
    while (n >= 0) {
        printf("%d ", n);
        n = n - index;
        index = n - index;
    }

    return 0;
}