#include <stdio.h>
#include <stdlib.h>
int sum(int x,int y)
{   int s=0,i;
    for(i=x;i<=y;i++)
        s+=i;    
    return(s);
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int s;
    s=sum(1,5); printf("%d",s);
    system("pause");
    return(0);
}

