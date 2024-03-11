#include <stdio.h>

int main()
{
	int a, b, c, d;
	int max = 0, min = 0;

	scanf("%d %d", &a, &b);

	if (a > b)
	{
		c = a;
		d = b;
	}
	else
	{
		c = b;
		d = a;
	}

	for (int i = 1;i <= d;i++)
	{
		if (c%i == 0 && d%i == 0)
		{
			if (max < i)	max = i;
		}
	}

	min = (a*b) / max;

	printf("%d\n%d", max, min);
	return 0;
}