#include <stdio.h>

int n, s, r;
int arr[20];

void solve(int i, int sum) {
    if (i >= n) {
        if (sum == s) r++;
        return;
    }

    solve(i + 1, sum + arr[i]);
    solve(i + 1, sum);
}

int main() {
    scanf("%d %d", &n, &s);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    solve(0, 0);

    if (!s) r--;
    printf("%d", r);

    return 0;
}
