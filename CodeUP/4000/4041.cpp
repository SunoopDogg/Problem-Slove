#include <stdio.h>

int main()
{
	int num, n[8] = { 0, }, sum[8] = { 0, };

	scanf("%d", &num);

	for (int i = 1000000;i >= 1;i /= 10)
	{
		n[0] = num / i;
		if (n[0] != 0)
		{
			sum[1] = n[0];
			n[1] = n[0];
			
			n[0] = num % i;
			if (n[0] == 0) break;
			n[0] = n[0] /( i / 10);
			sum[2] = n[0];
			n[2] = n[0] * 10;

			n[0] = num %( i / 10);
			if (n[0] == 0) break;
			n[0] = n[0] / (i / 100);
			sum[3] = n[0];
			n[3] = n[0] * 100;

			n[0] = num % (i / 100);
			if (n[0] == 0) break;
			n[0] = n[0] /( i / 1000);
			sum[4] = n[0];
			n[4] = n[0] * 1000;

			n[0] = num % (i / 1000);
			if (n[0] == 0) break;
			n[0] = n[0] / (i / 10000);
			sum[5] = n[0];
			n[5] = n[0] * 10000;

			n[0] = num %( i / 10000);
			if (n[0] == 0) break;
			n[0] = n[0] / (i / 100000);
			sum[6] = n[0];
			n[6] = n[0] * 100000;

			n[0] = num % (i / 100000);
			if (n[0] == 0) break;
			n[0] = n[0] / (i / 1000000);
			sum[7] = n[0];
			n[7] = n[0] * 1000000;
		}
	}
	
	for (int i = 1;i < 8;i++)
	{
		sum[0] += sum[i];
		n[0] += n[i];
	}

	printf("%d\n%d", n[0], sum[0]);
	return 0;
}