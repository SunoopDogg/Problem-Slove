#include <stdio.h>

int main()
{
	int a, b;
	int max = 0, sum = 0;;

	for (int i = 0;i < 4;i++)
	{
		scanf("%d %d", &a, &b);
		sum = sum - a + b;
		if (max < sum) max = sum;
	}

	printf("%d", max);
	return 0;
}