#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", (((n%137)*(n%137)+(n%137)+2)/2)%137);
    return 0;
}