#include <stdio.h>

int a, b, c, d;
int min = 11;

void f(int x, int A, int B)   {
    if(x > 10) return;
    
    if(A == c && B == d)
        if(min > x) {
            min = x;
            return;
        }
    
    f(x+1, a, B);
    f(x+1, A, b);
    f(x+1, A, 0);
    f(x+1, 0, B);
    if(A+B > a) f(x+1, a,  B-(a-A));
    else    f(x+1, A+B, 0);
    if(A+B > b) f(x+1, A-(b-B),  b);
    else    f(x+1, 0, A+B);
}

int main() {
    scanf("%d %d %d %d", &a, &b, &c ,&d);
    
    f(0, 0, 0);
    
    printf("%d", min == 11 ? -1 : min);
    return 0;
}