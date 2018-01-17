#include<stdio.h>
#include <string.h>
int main(){
	char s[] = "NSRQSWAWFYOMMGIYYYONFSPeterXIUEZITTCE";
	char t[] = "Peter";
	int head, window=5;
	int i, j, k, count, counter;
	
	counter = 0;
	for(head=0;head+window<strlen(s);head++){
		i = head;
		j = window;
		k = 0;
		count=0;

		while(1){
			if(count == 5){
				printf("%cPeter%c\n", s[i-6], s[i]);
				counter++;				
				break;
			}
			if(s[i] == t[k]){
			printf("good\n");
			i++;
			k++;
			count++;
			}
			
			else	break;
		}
	}
	printf("total %d", counter);
}
