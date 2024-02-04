#include <stdio.h>

int main()
{
    int a[10],b[10];
    int acnt=0,bcnt=0;
    
    for(int i=0;i<10;i++)
    {
    	scanf("%d",&a[i]);
    }
    for(int i=0;i<10;i++)
    {
    	scanf("%d",&b[i]);
    }
    
    for(int i=0;i<10;i++)
    {
    	if(a[i]>b[i])
    	{
    		acnt++;
    	}
    	else if(a[i]<b[i])
    	{
    		bcnt++;
    	}
    	
    }
    
    if(acnt>bcnt)
    {
    	printf("A");
    }
    else if (acnt<bcnt)
    {
    	printf("B");
    }
    else
    {
    	printf("D");
    }
    
    return 0;
}