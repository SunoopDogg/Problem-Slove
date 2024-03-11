#include <stdio.h>

int main()
{
	int a, b, c, d, x;
	int spc[100][100] = { 0, };
	int cnt = 0;
	
	for (int i = 0;i < 4;i++)
	{
		scanf("%d %d %d %d", &a, &b, &c, &d);
		x = 100 - d;
		for (int q = x;q < x + (d - b);q++)
		{
			for (int p = a;p < c;p++)
			{
				spc[q][p] = 1;
			}
		}
	}
	for (int i = 0;i < 100;i++)
	{
		for (int j = 0;j < 100;j++)
		{
			if (spc[i][j] == 1)	cnt++;
		}
	}
	printf("%d", cnt);
	return 0;
}