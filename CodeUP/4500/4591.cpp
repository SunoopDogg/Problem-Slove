#include <stdio.h>

int a[9] = { 0 };
int b[9] = { 0 };
int o = 0;

void set(int x)
{
	for (int i = 0;i < 9;i++)
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
	for (int i = 0; i < 9;i++)
	{
		scanf("%d", &a[i]);
		b[i] = a[i];
	}

	set(a[0]);

	o = 0;
	for (int i = 0;i < 9;i++)
	{
		if (a[0] == b[i])
		{
			break;
		}
		o++;
	}

	printf("%d\n", a[0]);
	printf("%d", o+1);

	return 0;
}