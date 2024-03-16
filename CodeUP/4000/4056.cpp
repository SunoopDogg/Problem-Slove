#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if(n <= 500) n *= 0.7;
    else if(n <= 1500)  n = 350 + (n-500) * 0.4;
    else if(n <= 4500)  n = 750 + (n-1500) * 0.15;
    else if(n <= 10000) n = 1200 + (n-4500) * 0.05;
    else    n = 1475 + (n-10000) * 0.02;
    printf("%d", n);
    return 0;
}