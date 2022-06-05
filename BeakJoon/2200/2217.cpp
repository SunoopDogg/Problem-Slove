#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return *(int *)b - *(int *)a; }

int main(void) {
    int n;
    int result = 0;

    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    qsort(arr, n, sizeof(int), compare);

    for (int i = 0; i < n; i++)
        if (arr[i] * (i + 1) > result) result = arr[i] * (i + 1);

    printf("%d\n", result);

    return 0;
}