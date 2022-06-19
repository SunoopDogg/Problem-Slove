#include <stdio.h>

int main() {
    int n;
    int max = 0;
    float total = 0;
    float arr[1001];

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%f", &arr[i]);
        total += arr[i];
        if (arr[i] > max) max = arr[i];
    }

    printf("%f\n", total / max * 100 / n);

    return 0;
}