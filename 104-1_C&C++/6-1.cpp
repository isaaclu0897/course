#include <stdio.h>
#include <stdlib.h>

int add(int x,int y)
{   int z;
    z=x+y;
    return(z);
}
//..............................................................................
int main( )
{   int a=3,b=4,c;
    c=add(a,b);
    printf("%d\n",c);
    
    system("pause");
    return(0);
}

