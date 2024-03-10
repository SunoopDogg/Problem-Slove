#include <stdio.h>

int main(void)
{
	int a, b, c;

	scanf("%d %d", &a, &b);

	c = b % 10;
	printf("%d\n", a*c);

	c = b / 10 % 10;
	printf("%d\n", a*c);

	c = b / 10 / 10 % 10;
	printf("%d\n", a*c);

	printf("%d", a*b);

	return 0;
}