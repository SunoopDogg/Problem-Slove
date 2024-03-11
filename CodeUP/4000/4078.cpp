#include <stdio.h>

int main() {
    char str[4];
    int n;
    
    scanf("%s%d\n", str, &n);
    for(int i = 0; i < n; i++, puts(""))  {
        char t[4];
        int s = 0, b = 0;
        scanf("%s\n", t);
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++)
                b += (str[i] == t[j]);
        for(int i = 0; i < 3; i++)
            s += (str[i] == t[i]);
        if(s)   printf("%dS", s);
        if(b-s)   printf("%dB", b-s);
        if(!s && !b)    printf("OUT");
        if(s == 3)  {
            printf("\nSUCCESS");
            return 0;
        }
    }
    printf("FAIL");
    return 0;
}