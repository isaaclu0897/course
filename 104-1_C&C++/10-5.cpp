#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{   int i;
    double x1,x2,dx,tol=1.e-10;
    x1=1000;
    x2=sqrt(2.+x1);
    i=0;
    dx=fabs(x1-x2);
    while(dx>tol)
    {   x1=x2;
        x2=sqrt(2.+x1);
        i++;
        dx=fabs(x1-x2);
        printf("i=%d x=%20.16f err=%20.16f\n",i,x2,2.-x2);
    }
    printf("%f",x2);
    
    system("pause");
    return(0);
}
 
