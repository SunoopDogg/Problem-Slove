#include <stdio.h>

int main()
{
	int a, b, m, n;

	scanf("%d %d", &n, &m);
	
	a = (n + m) / 2;
	b = (n - m) / 2;

	printf("%d\n%d", a, b);
	return 0;
}