#include <stdio.h>

int n;
int arr[1001][3];
int memo[1001][3];

int MIN(int a, int b)   {
	return a > b ? b : a;
}

int recur(int now, int count)   {
	int a, b;
	if(now == 0)  a = 1, b = 2;
	if(now == 1)  a = 0, b = 2;
	if(now == 2)  a = 0, b = 1;
	
	if(count == n-1)    return arr[count][now];
	
	if(memo[count][now]) return memo[count][now];
	else
		return memo[count][now] = MIN(arr[count][now] + recur(a, count+1), arr[count][now] + recur(b, count+1));
}

int main()  {
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++)
		for(int j = 0; j < 3; j++)
			scanf("%d", &arr[i][j]);
	
	printf("%d", MIN(MIN(recur(0, 0), recur(1, 0)), recur(2, 0)));
	
	return 0;
}
