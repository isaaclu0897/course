#include <stdio.h>
#include <stdlib.h>
void table9x9(int x,int y,int a,int b)
{   int i,j;
    
    for(i=x;i<=y;i++)
    {   for(j=a;j<=b;j++)
           printf("%d*%d=%2d\n",i,j,i*j);
        printf("\n");  
    }
      
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   table9x9(3,7,4,8);
    
    system("pause");
    return(0);
}
