#include <stdio.h>

int n, m, k;
int cnt;
int arr[16][16];

void f(int x, int y, int t) {
    if (x >= n || y >= m)  return;
    if (x == n - 1 && y == m - 1 && t)   cnt++;
    if (x * m + y + 1 == k)   t = 1;
    f(x + 1, y, t);
    f(x, y + 1, t);
}

int main() {
    scanf("%d %d %d", &n, &m, &k);
    f(0, 0, k ? 0 : 1);
    printf("%d", cnt);
    return 0;
}