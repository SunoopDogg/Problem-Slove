#include <stdio.h>

int main()
{
	int cnt, sum[3] = { 0, };

	for (int i = 0;i < 3;i++)
	{
		for (int j = 0;j < 4;j++)
		{
			scanf("%d", &cnt);
			sum[i] += cnt;
		}
	}

	for (int i = 0;i < 3;i++)
	{
		if (sum[i] == 1)	printf("C");
		else if (sum[i] == 2)	printf("B");
		else if (sum[i] == 3)	printf("A");
		else if (sum[i] == 4)	printf("E");
		else	printf("D");
		printf("\n");
	}

	return 0;
}