#include <stdio.h>

int main() {
    int n;
    int arr[500001][2], t = 0;

    scanf("%d", &n);
    for (int i = 0; i < n; i++, t++) {
        scanf("%d", &arr[t][0]);
        arr[t][1] = i;

        while (t && arr[t - 1][0] < arr[t][0]) {
            arr[t - 1][0] = arr[t][0];
            t--;
        }
        printf("%d ", arr[t][1]);
    }
    return 0;
}
