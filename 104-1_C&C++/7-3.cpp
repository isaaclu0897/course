#include <stdio.h>
#include <stdlib.h>
void rec(char ch,int m, int n)
{   int i,j;
    
    for(i=1;i<=m;i++)
    {   for(j=1;j<=n;j++)
        {   printf("%c",ch);
        }  
        printf("\n");
    }
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   rec('*',3,4);
    
    system("pause");
    return(0);
}
