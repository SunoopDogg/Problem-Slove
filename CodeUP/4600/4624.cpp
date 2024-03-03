#include <stdio.h>

int main() {
    char c1, c2;
    int arr[31], t = 0;
    int s = 0, a = 1;
    int p = 0, q = 0;
    
    while(scanf("%c", &c1) != EOF)   {
        if(c1 == '(')   {
            p++;
            a *= 2;
        }
        else if(c1 == ')')   {
            if(c2 == '(')   arr[t++] = a;
            p--;
            a /= 2;
        }
        else if(c1 == '[')  {
            q++;
            a *= 3;
        }
        else if(c1 == ']')   {
            if(c2 == '[')   arr[t++] = a;
            q--;
            a /= 3;
        }
        c2 = c1;
    }
    for(int i = 0; i++ < t;)
        s += arr[i-1];
    printf("%d", !p && !q ? s : 0);
    return 0;
}