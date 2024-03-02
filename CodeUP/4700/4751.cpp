#include <stdio.h>

struct play{
    int con;
    int num;
    int score;
};

int main(void)	{
    int n;
	int cnt = 0;
    int list[101] = { 0, };
    struct play p[101];
    
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++)  
        scanf("%d %d %d", &p[i].con, &p[i].num, &p[i].score);
	
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n - 1; j++)
	            if(p[j].score < p[j + 1].score) {
	                struct play tmp = p[j];
	                p[j] = p[j + 1];
	                p[j + 1]= tmp;
	            }
	
	for(int i = 0; i < n; i++)  {
	    if(list[p[i].con] == 2)
	        continue;
	    list[p[i].con]++;
	    cnt++;
        printf("%d %d\n", p[i].con, p[i].num);
        if(cnt == 3)
            break;
	}
	
	return 0;
}