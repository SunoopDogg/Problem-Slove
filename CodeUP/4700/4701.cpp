#include <stdio.h>
#include <stdlib.h>
#define abs(x) ((x) < 0 ? -(x) : (x))

arr[100001];

int compare(const void *a, const void *b)   {
    return *(int*)a > *(int*)b;
}

int main() {
    int n;
    int x, y;
    int i, j;
    int min = 1000000000;
    
    scanf("%d", &n);
    for(int q = 0; q < n; q++)
        scanf("%d ", &arr[q]);
    
    qsort(arr, n, sizeof(int), compare);
    
    for(int q = 0; q < n; q++)
        if(q > 0 && abs(arr[q]) < min) min = abs(arr[q]), i = q;
    j = i + 1;
    
    if(arr[0] >= 0){
        printf("%d %d", arr[0], arr[1]);
        return 0;
    }
    if(arr[n - 1] <= 0){
        printf("%d %d", arr[n - 2], arr[n - 1]);
        return 0;
    }
    
    while(1)    {
        if(abs(arr[i]+arr[j]) < abs(x + y))
            x = arr[i], y = arr[j];
        if(i == 0 && j == n-1)  break;
        if(arr[i] + arr[j] < 0 && j < n-1) j++;
        else if(i > 0)  i--;
    }
        
    printf("%d %d", x, y);
    
    return 0;
}