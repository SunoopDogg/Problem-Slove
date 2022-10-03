#include <stdio.h>

int main(void) {
    int N;

    scanf("%d", &N);

    int result = 1;
    for (int i = 1;; i++) {
        if (result >= N) {
            printf("%d", i);
            break;
        }
        result += i * 6;
    }

    return 0;
}