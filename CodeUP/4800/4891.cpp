#include <stdio.h>

int main(void)
{
	int n, m;
	int min = 1000, max = 0;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &m);
		if (min > m)
			min = m;
		if (max < m)
			max = m;
	}

	printf("%d", max - min);

	return 0;
}