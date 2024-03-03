#include <stdio.h>
 
int as1, as2[3];
int tr;
int cnt;
int maxcnt[3];
int count3[3];
int count2[3];
 
void set()
{
    for (int i = 0;i < 3;i++)
    {
        if (as2[i] < as2[i + 1])
        {
            tr = as2[i];
            as2[i] = as2[i + 1];
            as2[i + 1] = tr;
            set();
        }
    }
}
 
int main()
{   
    scanf("%d", &cnt);
 
    for (int i = 0; i < cnt; i++)
    {
        int q, w, e;
        scanf("%d %d %d", &q, &w, &e);
        maxcnt[0] += q;
        maxcnt[1] += w;
        maxcnt[2] += e;
 
        if (q == 3)count3[0]++;
        else if (q == 2)count2[0]++;
 
        if (w == 3)count3[1]++;
        else if (w == 2)count2[1]++;
 
        if (e == 3)count3[2]++;
        else if (e == 2)count2[2]++;
    }
 
    as2[0] = maxcnt[0];
    as2[1] = maxcnt[1];
    as2[2] = maxcnt[2];
    set();
     
    cnt=0;
 
    for (int i = 0;i < 3;i++)
    {
        if (as2[0] == maxcnt[i])
        {
            as1 = i+1;
            cnt++;
        }
    }
     
    if (cnt >= 2)
    {
        if (count3[0] > count3[1] && count3[0] > count3[2])       as1 = 1;
        else if (count3[1] > count3[0] && count3[1] > count3[2])      as1 = 2;
        else if (count3[2] > count3[1] && count3[2] > count3[0])      as1 = 3;
        else
        {
            if (count2[0] > count2[1] && count2[0] > count2[2])       as1 = 1;
            else if (count2[1] > count2[0] && count2[1] > count2[2])      as1 = 2;
            else if (count2[2] > count2[1] && count2[2] > count2[0])      as1 = 3;
            else        as1 = 0;
        }
    }
 
    printf("%d %d", as1, as2[0]);
 
    return 0;
}