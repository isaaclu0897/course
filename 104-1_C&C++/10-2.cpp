#include <stdio.h>
#include <stdlib.h>

int main( )
{   int s,i,m=10;

    for(s=0,i=0;s+i<=m;i++)
      s+=i;
    printf("Sum1=%d\n\n",i-1);//此法不合邏輯 

    s=0;
    i=0;
    while(s+i<=m)
    {  s+=i;
       i++;
    }
    i--;
    printf("Sum3=%d\n\n",i);
    
    s=0;
    i=0;
    do
    {  s+=i;
       i++;
    } while(s+i<=m);
    i--;
    printf("Sum4=%d\n\n",i);
   
    system("pause");
    return(0);
}
 
