#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main( )
{   double a,b,c,D; 
    
    printf("sol aX^2+bX+c=0, keyin a,b,c: ");
    scanf("%lf%lf%lf",&a,&b,&c);
    if(a!=0)
    {   printf("that is a 二元一次方程式\n");
        D=b*b-4*a*c;
        if     (D >0)   printf("相異實根 X1=%lf, X2=%lf",(-b+sqrt(D))/(2*a),(-b-sqrt(D))/(2*a));
        else if(D==0)   printf("重根     X1=X2=%lf",-b/(2*a));
        else            printf("共軛虛根 X1=%lf+i%lf,X2=%lf-i%lf",-2*b/(2*a),D/(2*a),-2*b/(2*a),D/(2*a));
    }
    else  
    {   if(b!=0)
        printf("X=%lf",-c/b);
        else
           if(c!=0)
           printf("no sol");
           else
           printf("inf sol");
    }
    
    system("pause");
    return(0);
}

