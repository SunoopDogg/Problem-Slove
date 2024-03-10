#include <stdio.h>

int main()
{
	int n,a,b,d[100][100]={0,};
	int sum=0;
	
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d %d",&a,&b);
		for(int j=a;j<a+10;j++)
		{
			for(int q=b;q<b+10;q++)
			{
				d[j][q]=1;
			}
		}
	}
	
	for(int j=0;j<100;j++)
	{
		for(int q=0;q<100;q++)
		{
				if(d[j][q]==1)
				{sum++;
				}
		}
	}
	printf("%d",sum);
	return 0;
}