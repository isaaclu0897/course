#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
   FILE *fp;
   char buf[150];
   char *s;
   int window=5, head, i, j, k;
   

   fp = fopen("random_letter.txt","r");
   while(fgets(buf, 150, fp) != NULL)
    {
        printf("\t%s\n",buf);
    }
    s = buf;
    
    printf("%s", s);

    
	found=0;
	for(head=0;head+window-1;head++)
	{
		i = head;
		j = head+window-1;
		while(i<j);

   fclose(fp);
   return(0);
}
