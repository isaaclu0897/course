#include <stdio.h>
#include <stdlib.h>
void sum_pro(int x,int y,int *ss,int *pp)
{    printf("2 %d %d %d %d\n",x,y,*ss,*pp);
     *ss=x+y;
     *pp=x*y;
     printf("3 %d %d %d %d\n",x,y,*ss,*pp);
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int a=2,b=3,s,p;
    printf("1 %d %d %d %d\n",a,b,s,p);
    system("pause");
    
    sum_pro(a,b,&s,&p);
    
    printf("4 %d %d %d %d\n",a,b,s,p);
    
    system("pause");
    return (0);    
}
