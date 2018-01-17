#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *f;
	f = freopen("random_letter.txt", "r", stdin);
	//freopen("HW4_2_104306012.txt", "w", stdout);

	char A[120];
	char B[1001];

	int i,j;

	scanf("%s",A);
	scanf("%s",B);

	while(fgets(A, 120, f) != NULL){
		for(i=0;A[i]<101;i++)
		{
			if (A[i]=='P'&&A[i+1]=='e'&&A[i+2]=='t'&&A[i+3]=='e'&&A[i+4]=='r')
			{
				printf("%c%c%c%c%c%c%c\n",A[i-1],A[i],A[i+1],A[i+2],A[i+3],A[i+4],A[i+5]);
			}
		}
	}
}
