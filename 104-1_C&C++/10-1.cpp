#include <stdio.h>
#include <stdlib.h>

int main( )
{   int s,i,n=5;

    for(s=0,i=0;i<=n;i++)
    {  s+=i;
       printf("sum1-%2d=%2d    i1-%2d=%2d\n",i,s,i,i);
    }
    printf("Sum1=%d\n\n",s);
   
    for(s=0,i=n;i>=1;i--)
    {   s+=i;
        printf("sum2-%2d=%2d    i2-%2d=%2d\n",i,s,i,i);
    }
    printf("Sum2=%d\n\n",s);

    s=0;
    i=0;
    while(i<=n)
    {  s+=i;
       i++;
       printf("sum3-%2d=%2d    i3-%2d=%2d\n",i,s,i,i);
    }
    printf("Sum3=%d\n\n",s);
    
    s=0;
    i=0;
    do
    {  s+=i;
       i++;
       printf("sum4-%2d=%2d    i4-%2d=%2d\n",i,s,i,i);
    } while(i<=n);
    printf("Sum4=%d\n",s);
   
    system("pause");
    return(0);
}
