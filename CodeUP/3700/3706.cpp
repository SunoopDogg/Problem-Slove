#include <stdio.h>

int main()  {
	int n;
	long long int a = 0, an = 0;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)   {
		a += i % 100000007;
		an += a % 100000007;
		an %= 100000007;
	}
	printf("%lld", an);
	return 0;
}