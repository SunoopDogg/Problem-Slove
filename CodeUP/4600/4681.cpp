#include <stdio.h>
int main()
{
	int a[5] = { 0 };
	int s = 0;

	for (int i = 0;i < 5;i++)
	{
		scanf("%d", &a[i]);
		s += a[i] * a[i];
	}
	s %= 10;
	printf("%d", s);

	return 0;
}