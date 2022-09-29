#include <stdio.h>

int main(void) {
    int X;

    scanf("%d", &X);

    int i, n;

    for (i = 1;; i++)
        if (2 * X <= i * (i + 1)) {
            n = (i * (i + 1)) / 2;
            break;
        }

    if (i % 2)
        printf("%d/%d", n - X + 1, i - (n - X));
    else
        printf("%d/%d", i - (n - X), n - X + 1);

    return 0;
}