#include <stdio.h>

int main(void) {
    int a, b, c;

    scanf("%4d.%2d.%2d", &a, &b, &c);
    printf("%02d-%02d-%04d", c, b, a);

    return 0;
}