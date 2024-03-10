#include <stdio.h>
int a[5];
int tmp;
void set()
{
	for(int i=0;i<4;i++)
	{
		if(a[i]<a[i+1])
		{
			tmp=a[i];
			a[i]=a[i+1];
			a[i+1]=tmp;
			set();
		}
	}
}
int main()
{
	int n;
	int max=0,tmp=0,mid=0;
	int sum=0;
	for(int i=0;i<5;i++)
	{
		scanf("%d",&a[i]);
		sum+=a[i];
	
	}
	set();
	printf("%d\n%d",sum/5,a[2]);
	
	return 0;
}