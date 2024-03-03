#include <stdio.h>

int main()
{
	int a,i,c=0,d=1;
	char b[100];
	
	scanf("%d",&a);
	
	for(i=0;i<=a;i++)
	{
		scanf("%d",&b[i]);
		
		if(b[i]!=0)
		{
			if(b[i-1]==b[i])
			{
				d++;
				c+=d;
			}
			
			else 
			{
				c+=1;
				d=1;
			}
		}
	}
	printf("%d",c);
	
	return 0;
}