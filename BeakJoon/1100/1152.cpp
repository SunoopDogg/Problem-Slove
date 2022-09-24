#include <stdio.h>

int main(void) {
    char str[1000001];
    int cnt = 0;
    int status = 0;

    scanf("%[^\n]s", str);

    for (int i = 0; str[i] != '\0'; i++)
        if (str[i] == ' ') {
            status = 0;
        } else if (!status) {
            status = 1;
            cnt++;
        }

    printf("%d", cnt);

    return 0;
}