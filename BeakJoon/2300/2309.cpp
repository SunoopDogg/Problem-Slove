#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return *(int *)a - *(int *)b; }

int main() {
    int arr[10];
    int sum = 0;

    for (int i = 0; i < 9; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    qsort(arr, 9, sizeof(int), compare);

    for (int i = 0; i < 9; i++)
        for (int j = i; j < 9; j++)
            if (i != j && sum - arr[i] - arr[j] == 100) {
                for (int q = 0; q < 9; q++)
                    if (q != i && q != j) printf("%d\n", arr[q]);
                return 0;
            }

    return 0;
}