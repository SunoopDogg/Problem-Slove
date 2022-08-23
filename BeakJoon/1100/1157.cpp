#include <stdio.h>

int main(void) {
    char c;
    int arr[26] = {0};

    while ((c = getchar()) != EOF) {
        if (c >= 'a' && c <= 'z')
            arr[c - 'a']++;
        else if (c >= 'A' && c <= 'Z')
            arr[c - 'A']++;
    }

    int max1 = 0, max2 = 0;
    int alpha;

    for (int i = 0; i < 26; i++) {
        if (arr[i] >= max1) {
            max2 = max1;
            max1 = arr[i];
            alpha = i;
        }
    }

    if (max1 == max2) {
        printf("?");
    } else {
        printf("%c", alpha + 'A');
    }

    return 0;
}