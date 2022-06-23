#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int m;
        int arr[1001];
        int sum = 0, cnt = 0;

        scanf("%d", &m);

        for (int j = 0; j < m; j++) {
            scanf("%d", &arr[j]);
            sum += arr[j];
        }

        for (int j = 0; j < m; j++)
            if ((float)sum / m < arr[j]) cnt++;

        printf("%.3f%\n", (float)cnt / m * 100);
    }

    return 0;
}