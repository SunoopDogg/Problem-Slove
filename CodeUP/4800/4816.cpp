#include <stdio.h>
#pragma warning(disable:4996)

int main(void)
{
	int t, time;
	int a = 0, b = 0, c = 0;

	scanf("%d", &t);
	time = t;
	if (t % 10 == 0)
	{
		for (int i = 0; i < time / 300; i++)
		{
			a++;
			t -= 300;
		}
		time = t;
		for (int i = 0; i < time / 60; i++)
		{
			b++;
			t -= 60;
		}
		time = t;
		for (int i = 0; i < time / 10; i++)
			c++;

		printf("%d %d %d", a, b, c);
	}
	else
		printf("-1");

	return 0;
}