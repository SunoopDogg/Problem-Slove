#include <stdio.h>

struct Soccer {
    int win;
    int tie;
    int lose;
    int rnk;
    int point;
};

int main()
{
    struct Soccer s[10001];
    int n,m,i,j;

    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {   s[i].rnk=1;
        scanf("%d %d %d",&s[i].win,&s[i].tie,&s[i].lose);
        s[i].point=3*s[i].win+s[i].tie;
    }

    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(s[i].point<s[j].point)
                s[i].rnk++;
        }
    }
    printf("%d",s[m-1].rnk);
}