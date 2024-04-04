#include <stdio.h>

int arr[52][52];

void g(int n, int m)   {
    if(m <= 0)  return;
    g(n, m-1);
    arr[n][m] = (arr[n][m-1] + arr[n-1][m])%100000000;
}

void f(int n, int m)   {
    if(n <= 0)  return;
    f(n-1, m);
    g(n, m);
}

int main() {
    int n, m;
    arr[0][1] = 1;
    scanf("%d %d", &n, &m);
    f(n, m);
    printf("%d", arr[n][m]);
    return 0;
}