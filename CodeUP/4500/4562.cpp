#include <stdio.h>

int main() {
    int n = 1;
    int arr[10] = { 0, };
    
    for(int i = 0; i < 3; i++)  {
        int t;
        scanf("%d", &t);
        n *= t;
    }
    while(n)    {
        arr[n%10]++;
        n /= 10;
    }
    for(int i = 0; i < 10; i++)
        printf("%d\n", arr[i]);
    return 0;
}