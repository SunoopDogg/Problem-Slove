#include <stdio.h>

int memo[10001] = { 1,1 };

int f(int n)   {
    if(memo[n]) return memo[n];
	return memo[n] = (f(n - 1) + f(n - 2) * 2) % 100007;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", f(n));
    return 0;
}