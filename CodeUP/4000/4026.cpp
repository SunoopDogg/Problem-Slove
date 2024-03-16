#include <stdio.h>

int main()
{
	int n;
	int max = 0, mid = 0, tmp = 0;

	for (int i = 0;i < 5;i++)
	{
		scanf("%d", &n);
		if (max < n)
		{
			mid = tmp;
			tmp = max;
			max = n;
		}
		else if (tmp < n)
		{
			mid = tmp;
			tmp = n;
		}
		else if (mid < n)
		{
			mid = n;
		}
	}
	
	printf("%d", mid);
	return 0;
}