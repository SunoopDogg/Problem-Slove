#include <stdio.h>

int main(void) {
    int n = 1;
    int arr[11] = {0};

    for (int i = 0; i < 3; i++) {
        int tmp;
        scanf("%d", &tmp);
        n *= tmp;
    }

    while (n) {
        arr[n % 10]++;
        n /= 10;
    }

    for (int i = 0; i < 10; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}