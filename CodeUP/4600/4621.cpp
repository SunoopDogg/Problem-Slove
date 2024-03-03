#include <stdio.h>

int main()
{
	int a, b, ans;
	int cnt = 0;
	
	scanf("%d %d", &a, &b);

	for (int i = 1;i <= a;i++)
	{
		if (a%i == 0)
		{
			cnt++;
			if (b == cnt)
			{
				ans = i;
				break;
			}
		}
	}

	if(cnt==0)	printf("0");
	else printf("%d", ans);
	
	return 0;
}