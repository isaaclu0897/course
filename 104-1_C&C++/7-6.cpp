#include <stdio.h>
#include <stdlib.h>
int main( )
{   int a,b,c,x,y;
    for(a=1;a<=9;a++)
       for(b=0;b<=9;b++)
          for(c=0;c<=9;c++)
          {   x=100*a+10*b+c;
              y=a*a*a+b*b*b+c*c*c;
              if(x==y)
                 printf("%d\n",x);
          }
    system("pause");
    return(0);
}
