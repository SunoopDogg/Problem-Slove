#include <stdio.h>

int main() {
    int n, cnt = 0;
    int arr[101][101] = { 0, };
    int x[] = { 0, 0, -1, 1 };
    int y[] = { -1, 1, 0, 0 };
    scanf("%d", &n);
    for(int i = 0; i < n; i++)  {
        int a, b;
        scanf("%d %d", &b, &a);
        for(int p = a; p < a+10; p++)
            for(int q = b; q < b+10; q++)
                arr[p][q] = 1;
    }
    for(int i = 1; i < 101; i++)
        for(int j = 1; j < 101; j++)
            if(arr[i][j])
                for(int k = 0; k < 4; k++)
                    if(!arr[i+x[k]][j+y[k]])
                        cnt++;
    printf("%d", cnt);
    return 0;
}