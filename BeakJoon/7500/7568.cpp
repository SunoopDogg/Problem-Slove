#include <stdio.h>

int main() {
    int n;
    int arr[51][3] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d %d", &arr[i][0], &arr[i][1]);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            arr[i][2] += arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1];
        printf("%d\n", arr[i][2] + 1);
    }

    return 0;
}