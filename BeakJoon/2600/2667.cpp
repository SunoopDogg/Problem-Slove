#include <stdio.h>
#include <stdlib.h>

int n, cnt;
int arr[27][27];
int s[101];

void f(int x, int y) {
    if (!arr[x][y]) return;

    arr[x][y] = 0;
    s[cnt]++;
    f(x - 1, y);
    f(x + 1, y);
    f(x, y - 1);
    f(x, y + 1);
}

int compare(const void *a, const void *b) { return *(int *)a - *(int *)b; }

int main() {
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        char str[26];
        scanf("%s", str);
        for (int j = 0; str[j] != '\0'; j++) arr[i][j + 1] = str[j] - 48;
    }

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (arr[i][j]) {
                f(i, j);
                cnt++;
            }
    qsort(s, cnt, sizeof(int), compare);

    printf("%d\n", cnt);
    for (int i = 0; i < cnt; i++) printf("%d\n", s[i]);

    return 0;
}
