#include <stdio.h>

int memo[10001] = { 0,0,0,2 };

int f(int n)   {
    if(memo[n]) return memo[n];
	if(n == 1 || n == 2) return 0;
	return memo[n] = (f(n - 3) * 2) % 100000007;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", f(n));
    return 0;
}