#include <stdio.h>

int arr[41][2] = {{1, 0}, {0, 1}};

int get_0(int N) {
    if (N == 0)
        return 1;
    else if (N == 1)
        return 0;
    if (!arr[N][0]) arr[N][0] = get_0(N - 1) + get_0(N - 2);
    return arr[N][0];
}

int get_1(int N) {
    if (N == 0)
        return 0;
    else if (N == 1)
        return 1;
    if (!arr[N][1]) arr[N][1] = get_1(N - 1) + get_1(N - 2);
    return arr[N][1];
}

int main(void) {
    int T;

    scanf("%d", &T);

    while (T--) {
        int N;

        scanf("%d", &N);

        arr[N][0] = get_0(N);
        arr[N][1] = get_1(N);
        printf("%d %d\n", arr[N][0], arr[N][1]);
    }

    return 0;
}