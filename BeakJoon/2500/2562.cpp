#include <stdio.h>

int main() {
    int max = 0;
    int index = 0;

    for (int i = 0; i < 9; i++) {
        int n;

        scanf("%d", &n);
        if (n > max) {
            max = n;
            index = i;
        }
    }

    printf("%d\n%d", max, index + 1);

    return 0;
}