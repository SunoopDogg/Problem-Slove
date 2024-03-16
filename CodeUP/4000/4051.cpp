#include <stdio.h>

int main(void)
{
	int i,j;
	float a,b,c,d=0,e=0;

	for(i=1;i<=5;i++)
	{
		scanf("%f %f",&a,&b);
		c=b-a-1;
		if(c<=0)
		{
			d=d+0;
		}
		else if(c>=4)
		{
			d=d+4;
		}
		else
		{
			d=d+b-a-1;
		}
	}
	
	if(d>=15)
	{
		e=d*5000/0.5;
		e=e-e*0.05;
		printf("%.lf",e);
	}
	else if(d<=5)
	{
		e=d*5000/0.5;
		e=e+e*0.05;
		printf("%.lf",e);
	}
	else
	{
		printf("%.lf",d*5000/0.5);
	}
	
	return 0;
}