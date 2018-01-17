#include <stdio.h>
#include <string.h>
int main(void)
{
	int window;
	int head;
	int i,j,k;
	int found;
	char word[1000];
	printf("enter a string:");
	scanf("%s",word);
	for (window=strlen(word);window>=2;window--)
	{
		found = 0;
		for(head=0;head+window-1<strlen(word);head++)
		{
			i=head;
			j=head+window-1;
			while(i<j)
			{
				if(word[i]==word[j])
				{
					i++;
					j--;
				}
				else
				{
					break;
				}
			}
			if(i>j)
			{
				for(k=head;k<=head+window-1;k++)
				{
					printf("%c",word[k]);
				}
				printf("\n");
				found = 1;
			}
		}
		if(found) break;
	}
	return 0;
}
