#include <stdio.h>

int memo[10001][10001];

int f(int n, int r)   {
    if(memo[n][r]) return memo[n][r];
    if(r==0 || n==r)    return 1;
    return memo[n][r] = (f(n-1, r-1)+f(n-1, r))%100000007;
}

int main() {
    int n, r;
    scanf("%d %d", &n, &r);
    printf("%d", f(n, r));
    return 0;
}