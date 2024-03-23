#include <stdio.h>

int main()
{
	int n, sum = 0;

	for (int i = 0;i < 7;i++)
	{
		scanf("%d", &n);
		if (n % 2 == 1)
		{
			sum += n;
		}
	}
	
	if (sum == 0)	printf("-1");
	else printf("%d", sum);

	return 0;
}
