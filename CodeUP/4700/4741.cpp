#include <stdio.h>

int main()
{
	int h,m,t;
	
	scanf("%d %d %d",&h,&m,&t);
	
	m=h*60+m+t;
	m%=1440;
	printf("%d %d",m/60,m%60);
	
	return 0;
}