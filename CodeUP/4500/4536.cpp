#include <stdio.h>

int main() {
    int n;
    int sum = 0, max = 0;;
    int arr[101] = { 0, };
    
    for(int i = 0; i < 10; i++){
        int num;
        scanf("%d", &num);
        sum += num;
        arr[num/10]++;
    }
    
    for(int i = 0; i < 101; i++)
        if(arr[i] > arr[max])
            max = i;
    
    printf("%d\n%d", sum/10, max*10);
    
    return 0;
}