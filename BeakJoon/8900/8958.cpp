#include <stdio.h>

int main() {
    int n;
    char str[81];

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int score = 0;
        int cnt = 0;

        scanf("%s", str);

        for (int j = 0; str[j] != '\0'; j++) {
            if (str[j] == 'O')
                cnt++;
            else if (str[j] == 'X')
                cnt = 0;

            score += cnt;
        }

        printf("%d\n", score);
    }

    return 0;
}