#include <stdio.h>

int main(void) {
    int num, temp;
    int min = 1000000, max = -1000000;

    scanf("%d", &num);

    for (int i = 0; i < num; i++) {
        scanf("%d", &temp);
        if (temp > max) max = temp;
        if (temp < min) min = temp;
    }

    printf("%d %d", min, max);

    return 0;
}