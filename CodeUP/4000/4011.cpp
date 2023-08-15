#include <stdio.h>

int main() {
    int a, b;
    int mf;
    int y, m, d;
    char s;

    scanf("%d-%d", &a, &b);

    mf = b / 1000000;

    y = a / 10000;
    if (mf < 3)
        y += 1900;
    else
        y += 2000;

    m = a % 10000;
    m = m / 100;

    d = a % 100;

    if (mf % 2 == 0)
        s = 'F';
    else
        s = 'M';

    printf("%d/%02d/%02d %c", y, m, d, s);

    return 0;
}