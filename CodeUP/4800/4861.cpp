#include <stdio.h>

int main() {
    int n, k;
    int arr[7][2] = { 0, };
    int result = 0;
    
    scanf("%d %d", &n, &k);
    
    for(int i = 0; i < n; i++)  {
        int s, y;
        scanf("%d %d", &s, &y);
        arr[y][s]++;
    }
    
    for(int i = 1; i < 7; i++)  {
        result += arr[i][0] / k;
        if(arr[i][0] % k != 0) result++;
        result += arr[i][1] / k;
        if(arr[i][1] % k != 0) result++;
    }
    
    printf("%d", result);
    return 0;
}