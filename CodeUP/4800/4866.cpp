#include <stdio.h>

int main(void)
{
	int n, k, a, b;
	int arr[5] = { 0 };
	int cnt = 0;

	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &a, &b);
		if (b - 1 == 0 || b - 1 == 1)
			a = 0;
		else if (b - 1 == 2 || b - 1 == 3)
			if (a == 0)
				a = 1;
			else
				a = 2;
		else
			if (a == 0)
				a = 3;
			else
				a = 4;
		arr[a]++;
		if (arr[a] == 1)
			cnt++;
		if (arr[a] == k)
			arr[a] = 0;
	}
	
	printf("%d", cnt);

	return 0;
}