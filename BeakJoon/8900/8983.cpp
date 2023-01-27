#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    const int* arg1;
    const int* arg2;

    return *(int*)a - *(int*)b;
}

int main() {
    int m, n, l, x, y, cnt = 0;
    int arr[100001];

    scanf("%d %d %d", &m, &n, &l);

    for (int i = 0; i < m; i++) scanf("%d ", &arr[i]);

    qsort(arr, m, sizeof(int), compare);

    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        int up = x + l - y, down = x + y - l, left = 0, right = m - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (down <= arr[mid] && arr[mid] <= up) {
                cnt++;
                break;
            } else if (arr[mid] < down)
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    printf("%d\n", cnt);
}