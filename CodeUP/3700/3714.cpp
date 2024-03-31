#include <stdio.h>

int memo[10001] = { 0,1,5,11 };

int f(int n)   {
    if(memo[n]) return memo[n];
	return memo[n] = (f(n - 1) + f(n - 2) * 4 + f(n - 3) * 2) % 100007;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", f(n));
    return 0;
}