#include <stdio.h>

int main(void) {
    int N;
    int result = 0;

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        char str[101];
        int arr[26] = {0};

        scanf("%s", str);

        char prev = str[0];
        arr[prev - 'a']++;
        for (int j = 1; str[j] != '\0'; j++)
            if (prev != str[j]) {
                prev = str[j];
                if (!arr[str[j] - 'a'])
                    arr[str[j] - 'a']++;
                else {
                    result--;
                    break;
                }
            }
        result++;
    }

    printf("%d", result);

    return 0;
}