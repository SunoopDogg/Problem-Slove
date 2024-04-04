#include <stdio.h>

long long int arr[52][52];

void g(int x, int y)   {
    if(y <= 0)  return;
    g(x, y-1);
    printf("%lld ", arr[x][y] = arr[x-1][y-1] + arr[x-1][y]);
}

void f(int n)   {
    if(n <= 0)  return;
    f(n-1);
    g(n, n);
    printf("\n");
}

int main() {
    int n;
    arr[0][0] = 1;
    scanf("%d", &n);
    f(n);
    return 0;
}