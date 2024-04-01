#include <stdio.h>

int memo[10001] = { 0,1,2 };

int f(int n)   {
    if(memo[n])
        return memo[n];
    else
        return memo[n] = (f(n-2) + f(n-1)) % 100000007;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", f(n));
    return 0;
}