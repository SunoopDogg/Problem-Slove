#include <stdio.h>

int a[7] = {0};
int o = 0;

void set(int x)
{
	for (int i = 0;i < 7;i++)
	{
		if (a[i] < a[i + 1])
		{
			o = a[i];
			a[i] = a[i + 1];
			a[i + 1] = o;
			set(a[i]);
		}
	}
	return;
}

int main()
{
	for (int i = 0; i < 7;i++)
	{
		scanf("%d",&a[i] );
	}

	set(a[0]);

	printf("%d\n", a[0]);
	printf("%d", a[1]);

	return 0;
}