#include <stdio.h>

int arr[301];
int memo[301];

int cmp(int a, int b)   {
    return a > b ? a : b;
}

int f(int n)   {
    if(n < 0)   return 0;
    else if(n == 1) return memo[1] = arr[1];
    else if(n == 2) return memo[2] = arr[1] + arr[2];
    if(memo[n]) return memo[n];
    else    return memo[n] = cmp(f(n-3)+arr[n-1], f(n-2)) + arr[n];
}

int main() {
    int n;
    scanf("%d", &n);
    for(int  i = 1; i <= n; i++)
        scanf("%d", &arr[i]);
    printf("%d", f(n));
    return 0;
}