#include <stdio.h>

int main()
{
	int a,b,c=0,d=0,i,j;
	
	scanf("%d %d",&a,&b);
	
	for(i=a;i<=b;i++)
	{
		for(j=2;j<i;j++)
		{
			if(!(i%j))	goto A;
		}
		if(!c&&i!=1)c=i;
		if(i!=1)d+=i;
		A:;
	}
	printf("%d\n%d",d,c);
}