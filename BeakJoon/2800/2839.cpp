#include <stdio.h>

int main(void) {
    int n;
    int result = 0;

    scanf("%d", &n);

    while (n >= 0) {
        if (n % 5 == 0) {
            result += n / 5;
            n = 0;
            break;
        }
        n -= 3;
        result++;
    }

    printf("%d\n", n ? -1 : result);

    return 0;
}