#include <stdio.h>
#include <math.h>

int main(void)
{
	int a, b;
	int cnt = 0;
	int min = 100000, max = 0;

	scanf("%d %d", &a, &b);

	if (a > b)
	{
		int tmp = a;
		a = b;
		b = tmp;
	}

	for (int i = a; i <= b; i++)
	{
		int flag = 1;

		for (int j = 2; j <= sqrt(i); j++)
			if (!(i % j))
			{
				flag = 0;
				break;
			}

		if (flag)
		{
			cnt++;

			if (i < min)
				min = i;
			if (i > max)
				max = i;
		}
	}

	printf("%d\n", cnt);
	printf("%d", min + max);

	return 0;
}