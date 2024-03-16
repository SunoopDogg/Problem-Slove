#include <stdio.h>

int main()
{
	int n;
	
	scanf("%d",&n);
	
	for(int i=2;i<=n;i++)
	{
		int a=1;
		
		if(n%i==0)
		{
			if(i==2)
			{
				printf("%d ",i);
				n/=i;
				i=1;
			}
			else
			{
				for(int j=2;i<j;j++)
				{
					if(i%j==0)
					{
						a=0;
						break;
					}
				}
				if(a==1)
				{
					printf("%d ",i);
					n/=i;
					i=1;
				}
			}
		}
	}

	return 0;
}