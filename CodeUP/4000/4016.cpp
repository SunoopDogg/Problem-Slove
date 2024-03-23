#include <stdio.h>

int main()
{
	int a,b,c,d;
	
	scanf("%d %d %d",&a,&b,&c);
	d=c;
	while(!(a%d==0&&b%d==0&&c%d==0))d--;
	printf("%d",d);
	
	return 0;
}