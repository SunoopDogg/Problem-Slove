#include <stdio.h>

int m, n;
int arr[8];

void backTrack(int x) {
    if (x >= n) {
        for (int i = 0; i < n; i++) printf("%d ", arr[i]);
        printf("\n");
        return;
    }

    for (int i = 0; i < m; i++) {
        arr[x] = i + 1;
        backTrack(x + 1);
    }
}

int main(void) {
    scanf("%d %d", &m, &n);

    backTrack(0);

    return 0;
}