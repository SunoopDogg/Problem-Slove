#include <stdio.h>

int main() {
    int n, m;
    int arr[100001];
    int max = -201;
    
    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    if(n == m)  {
        int sum = 0;
        for(int i = 0; i < n; i++)
            sum += arr[i];
        printf("%d", sum);
        return 0;
    }
    else
        for(int i = 0; i <= n - m; i++)  {
            int sum = 0;
            for(int j = 0; j < m; j++)
                sum += arr[i+j];
            if(sum > max) max = sum;
        }
            
    printf("%d", max);
    
    return 0;
}