#include <stdio.h>

int main() {
    int arr[42] = {0};
    int cnt = 0;

    for (int i = 0; i < 10; i++) {
        int n;
        scanf("%d", &n);

        if (!arr[n % 42]++) cnt++;
    }

    printf("%d\n", cnt);

    return 0;
}