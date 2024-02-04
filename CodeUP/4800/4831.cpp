#include <stdio.h>

int main()
{
    int n, a, c=0;
    scanf("%d", &n);
    for(int i = 0; i < 5; i++)
    {
        scanf("%d", &a);
        if (a==n) c++;
    }
    printf("%d", c);
    return 0;
}