#include <stdio.h>

int main(void)  {
    int n, m, x, y;
    int arr[250][250] = { 0, };
    int result = 0;
    
    scanf("%d %d %d %d", &m, &n, &x, &y);
    
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            scanf("%d ", &arr[i][j]);
            
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)  {
            int sum = 0;
            for(int k = 0; k < y; k++)
                for(int l = 0; l < x; l++)
                    sum += arr[i+k][j+l];
            if(sum > result)    result = sum;
        }
        
    printf("%d", result);
    
    return 0;
}