#include <stdio.h>

int main()
{
	int n[5][5];
	int max=0;
	int sum1=0,sum2=0;
	
	for(int i=0;i<5;i++)
	{
		for(int j=0;j<5;j++)
		{
			scanf("%d",&n[i][j]);
			if(max<n[i][j])
			{
				max=n[i][j];
			}
		}
		sum1+=max;
		max=0;
	}
	
	for(int i=0;i<5;i++)
	{
		for(int j=0;j<5;j++)
		{
			if(max<n[j][i])
			{
				max=n[j][i];
			}
		}
		sum2+=max;
		max=0;
	}
	
	if(sum1-sum2>0)
	{
		printf("%d",sum1-sum2);
	}
	else
	{
		printf("%d",sum2-sum1);
	}
	
    return 0;
}