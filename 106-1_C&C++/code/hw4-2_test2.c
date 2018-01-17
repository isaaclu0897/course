#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main (){
	FILE *fp_r, *fp_w;
	char s[150];
	char t[]="Peter";
	int h, l=5, c1, c2=0;
	int i, j, k;
	fp_r = freopen("random_letter.txt","r", stdin);
	freopen("HW4_2_104306033.txt", "w", stdout);
	printf("this is homework4-2 of 104306033\n\n");
	while(fgets(s, 150, fp_r) != NULL){
		for(h=0;h+l<strl(s);h++){
			i = h;
			j = l;
			k = 0;
			c1=0;
			while(1){
				if(c1 == strl(t)){
					printf("%cPeter%c\n", s[i-6], s[i]);
					c2++;				
					break;
				}
				if(s[i] == t[k]){
					i++;
					k++;
					c1++;
				}
				else	break;
			}
		}
	}
	printf("\ntotal find %d of Peter\n", c2);
	fclose(stdin);
	fclose(stdout);
	return(0);
}
