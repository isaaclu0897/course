#include <stdio.h>
#include <stdlib.h>
void utri(char ch,int m)
{   int i,j;
    
    for(i=1;i<=m;i++)
    {   for(j=1;j<=i;j++)
        {   printf("%c",ch);
        }  
        printf("\n");
    }
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   utri('*',3);
    
    system("pause");
    return(0);
}
