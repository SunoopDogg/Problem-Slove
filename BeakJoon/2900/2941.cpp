#include <stdio.h>

int main(void) {
    char str[101];
    int result = 0;

    scanf("%s", str);

    for (int i = 0; str[i] != '\0'; i++) {
        result++;
        if (str[i] == 'j') {
            if (str[i - 1] == 'l' || str[i - 1] == 'n') result--;
        } else if (str[i] == '-') {
            if (str[i - 1] == 'c' || str[i - 1] == 'd') result--;
        } else if (str[i] == '=') {
            if (str[i - 1] == 'c' || str[i - 1] == 's' || str[i - 1] == 'z') {
                result--;
                if (str[i - 1] == 'z' && str[i - 2] == 'd') result--;
            }
        }
    }

    printf("%d", result);

    return 0;
}