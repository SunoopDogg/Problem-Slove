#include <stdio.h>

int main()
{
	int n,a,b;
	
	scanf("%d",&n);
	n%=60;
	a=n%10;
	a+=6;
	if(a>9)
	{
		a%=10;
	}
	b=n%12;
	b-=4;
	if(b<1)
	{
		b=12+b;
	}
	printf("%c%d",b+65,a);
	return 0;
}