#include <stdio.h>

int main(void) {
    char S[101];
    int arr[26] = {0};

    scanf("%s", S);

    for (int i = 0; S[i] != '\0'; i++)
        if (!arr[S[i] - 'a']) arr[S[i] - 'a'] = i + 1;

    for (int i = 0; i < 26; i++) printf("%d ", arr[i] - 1);

    return 0;
}