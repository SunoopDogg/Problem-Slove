#include <stdio.h>

long long int memo[10000001];

long long int f(long long int n)   {
    if(n == 1)  return 1;
    if(n >= 10000000){
		if(n%2) return 1 + f(3*n+1);
		else return 1 + f(n/2);
	}
    if(memo[n]) return memo[n];
    if(n%2)    return memo[n] = 1 + f(3*n+1);
    else    return memo[n] = 1 + f(n/2);
}

int main() {
    int a, b, n;
    long long int max = 0;
    scanf("%d %d", &a, &b);
    
    for(int i = a; i <= b; i++) {
        long long int cnt = f(i);
        if(cnt > max)   {
            n = i;
            max = cnt;
        }
    }
    
    printf("%d %lld", n, max);
    return 0;
}