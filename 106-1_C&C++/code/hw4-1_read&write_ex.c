#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
        FILE *f;
        char c;
   
	f = freopen("file.txt", "r", stdin);

	while (feof(f)){
		c = fgetc(f);
		
		printf("%c", c);
	}


	
	//char *s="That‘s good news";
	//f = freopen("old.txt", "w+", stdout);

	//fprintf(f, "%s", s);

        fclose(stdin);
     
        return 0;
}
