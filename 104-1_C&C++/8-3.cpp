#include <stdio.h>
#include <stdlib.h>
int swap(int *x,int *y)
{    int tmp;

     tmp=*x;
     *x=*y;
     *y=tmp;
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int a=2,b=3,tmp;
    
    swap(&a,&b);
    printf("%d %d\n",a,b);
    
    system("pause");
    return (0);    
}
