#include <stdio.h>
 
int a,c[5];
int tmp,money,max=0;
 
void set()
{
    for (int j = 0;j < 4;j++)
    {
        if (c[j] < c[j+1])
        {
            tmp = c[j];
            c[j] = c[j + 1];
            c[j + 1] = tmp;
            set();
        }
    }
}
 
int main()
{
    scanf("%d", &a);
    for (int i = 0;i< a;i++)
    {
        for (int j = 0;j < 4;j++)    scanf("%d ", &c[j]);
        set();
        if (c[0] == c[3])   money = 50000 + c[0] * 5000;
        else if (c[0] == c[2] || c[1] == c[3])  money = 10000 + c[1] * 1000;
        else if (c[0] == c[1] && c[2] == c[3])  money = 2000 + c[0] * 500 + c[2] * 500;
        else if (c[0] == c[1])  money = 1000 + c[0] * 100;
        else if (c[1] == c[2])  money = 1000 + c[1] * 100;
        else if (c[2] == c[3])  money = 1000 + c[2] * 100;
        else money = c[0] * 100;
        if (max < money)max = money;
    }
 
    printf("%d", max);
 
    return 0;
}