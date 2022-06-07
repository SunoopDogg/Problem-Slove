#include <stdio.h>
#include <string.h>

int main(void) {
    char str[8];
    int num = 0, max = 0;

    scanf("%s", &str);
    for (int i = 0; i < strlen(str); i++) {
        num *= 10;
        num += str[i] - '0';
    }

    num -= strlen(str) * 9;

    for (int i = 0; i < strlen(str) * 9; i++) {
        int tmp = num + i;
        int sum = tmp;

        while (tmp > 0) {
            sum += tmp % 10;
            tmp /= 10;
        }

        if (sum == num + strlen(str) * 9) {
            printf("%d\n", num + i);
            return 0;
            break;
        }
    }

    printf("0\n");
    return 0;
}