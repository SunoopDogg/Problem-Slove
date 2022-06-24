#include <stdio.h>

int main() {
    int n;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int m;
        char str[21];

        scanf("%d %s", &m, str);

        for (int p = 0; str[p] != '\0'; p++)
            for (int q = 0; q < m; q++) printf("%c", str[p]);
        printf("\n");
    }

    return 0;
}