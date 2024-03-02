#include <stdio.h>
#include <string.h>

int main()
{
	char str[99];
	int sum = 0;

	scanf("%s", &str);

	for (int i = 0;i < strlen(str);i++)
	{
		if (str[i] == str[i+1])	sum += 5;
		else sum += 10;
	}

	printf("%d", sum);

	return 0;
}