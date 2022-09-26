#include <stdio.h>

int main(void) {
    int N;
    int result = 0;

    scanf("%d", &N);
    getchar();

    for (int i = 0; i < N; i++) {
        char temp;
        scanf("%c", &temp);
        result += temp - '0';
    }

    printf("%d", result);

    return 0;
}