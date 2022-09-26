#include <stdio.h>

int main(void) {
    int A, B, a = 0, b = 0;

    scanf("%d %d", &A, &B);

    while (A) {
        a *= 10;
        a += A % 10;
        A /= 10;
    }

    while (B) {
        b *= 10;
        b += B % 10;
        B /= 10;
    }

    printf("%d", a > b ? a : b);

    return 0;
}