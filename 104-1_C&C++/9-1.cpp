#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main( )
{   int n=5,i;
    double A[5]={50,60,70,80,90},s,avg,sigma;
    
    for(s=0,i=0;i<n;i++)
        s+=A[i];
    avg=s/n;
    
    for(s=0,i=0;i<n;i++)
        s+=pow(A[i]-avg,2);
    sigma=sqrt(s/(n-1));
    
    printf("It is avg %f\nIt is sigma %f\n",avg,sigma);
    
    system("pause");
    return(0);
}
