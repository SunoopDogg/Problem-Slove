#include <stdio.h>

int main()
{
	int n,a,b;
	int max=0;
	
    for(int i=0;i<9;i++)
    {
    	for(int j=0;j<9;j++)
    	{
    		scanf("%d",&n);
    		if(max<n)
    		{
    			max=n;
    			a=i;
    			b=j;
    		}
    	}
    }
    
    printf("%d\n%d %d",max,a+1,b+1);
    
    return 0;
}