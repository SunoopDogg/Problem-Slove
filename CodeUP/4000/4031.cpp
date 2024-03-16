#include <stdio.h>

int main()
{
	int a, max1 = 0, max2 = 0;

	for (int i = 0;i < 7;i++)
	{
		scanf("%d", &a);
		if (a % 2 == 0)
		{
			if (max1 < a)	max1 = a;
		}
		else
		{
			if (max2 < a)	max2 = a;
		}
	}

	printf("%d", max1 + max2);
	return 0;
}