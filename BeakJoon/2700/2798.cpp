#include <stdio.h>

int n, m;
int arr[101];
int max;

void f(int x, int sum, int cnt) {
    if (x > n || sum > m || cnt > 3) return;
    if (sum > max && cnt == 3) max = sum;

    f(x + 1, sum + arr[x], cnt + 1);
    f(x + 1, sum, cnt);
}

int main(void) {
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    f(0, 0, 0);

    printf("%d\n", max);

    return 0;
}