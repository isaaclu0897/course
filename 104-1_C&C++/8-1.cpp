#include <stdio.h>
#include <stdlib.h>
int sum(int x,int y)
{   printf("%d %d\n",x,y);
    return(x+y);
    printf("%d %d\n",x,y);
}
int pro(int x,int y)
{   printf("%d %d\n",x,y);
        return(x*y);
    printf("%d %d\n",x,y);
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int a=2,b=3,s,p;
    printf("%d %d %d %d\n",a,b,s,p);
    system("pause");
    
    s=sum(a,b);
    p=pro(a,b);
    printf("%d %d %d %d\n",a,b,s,p);
    
    system("pause");
    return (0);    
}
