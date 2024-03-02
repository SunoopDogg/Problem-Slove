#include <stdio.h>

int a,b;
int cnt3[3];
int cnt2[3];
int sum[3];
int m,m2,s1,s2;

int main()
{
	scanf("%d", &a);
	for (int i = 0;i< a;i++)
	{
		for (int j = 0;j < 3;j++) {
			scanf("%d",&b);
			sum[j] += b;
			if (b == 3) cnt3[j]++;
			else if (b == 2) cnt2[j]++;
			if (m <= sum[j]) {
				m2 = m;
				s2 = s1;
				m = sum[j];
				s1 = j;
			}
		}
	}
	if (m == m2)
	{
		if (cnt3[s1] > cnt3[s2])	a = s1+1;
		else if (cnt3[s1] < cnt3[s2]) a = s2+1;
		else {
			if (cnt2[s1] > cnt2[s2])	a = s1+1;
			else if (cnt2[s1] < cnt2[s2])	a = s2+1;
			else 	a = 0;
		}
	}
	else a = s1+1;

	printf("%d %d", a, m);

	return 0;
}