#include <stdio.h>

int main(void)
{
	int a,b=0,i,j;
	char c[100];
	
	scanf("%d",&a);

	j=a;
	
	for(i=0;a>0;i++)
	{
		c[i]=a%2;
		a=a/2;
		b++;
	}
	
	printf("2 ");
	
	for(i=b-1;i>=0;i--)
	{
		printf("%d",c[i]);//2
	}

	printf("\n8 %o\n",j);//8
	printf("16 %X",j);//16
	
	return 0;
}