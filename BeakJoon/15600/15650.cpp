#include <stdio.h>

int m, n;
int arr[8];
int visited[8];

void backTrack(int x, int y) {
    if (x >= n) {
        for (int i = 0; i < n; i++) printf("%d ", arr[i]);
        printf("\n");
        return;
    }

    for (int i = y; i < m; i++)
        if (!visited[i]) {
            visited[i] = 1;
            arr[x] = i + 1;
            backTrack(x + 1, i + 1);
            visited[i] = 0;
        }
}

int main(void) {
    scanf("%d %d", &m, &n);

    backTrack(0, 0);

    return 0;
}