#include <stdio.h>
int main()
{
    int base[21] = { 0, };
    int a = 0, b = 0;
    int tmp = 0;
 
    for (int i = 1;i < 21;i++)
    {
        base[i] = i ;
    }
 
    for (int i = 0;i < 10;i++)
    {
        scanf("%d %d", &a, &b);
 
        for (int j = a;j <= (a + b - 1) / 2;j++)
        {
            tmp = base[j];
            base[j] = base[a + b - j];
            base[a + b - j] = tmp;
        }
    }
 
    for (int i = 1;i < 21;i++)
    {
        printf("%d ", base[i]);
    }
     
    return 0;
}