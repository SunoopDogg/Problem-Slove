#include <stdio.h>

int main() {
    int h, m , s;
    int n;
    
    scanf("%d %d %d", &h, &m ,&s);
    scanf("%d", &n);
    
    n += h*60*60+m*60+s;
    
    h = n/(60*60);
    n %= 60*60;
    m = n/60;
    n %= 60;
    
    printf("%d %d %d", h%24, m, n);
    
    return 0;
}