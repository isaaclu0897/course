#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void avg_sig(double X[],int n,double *avg,double *sig)
{   int i;
    double s;
    for(s=0,i=0;i<n;i++)
        s+=X[i];
    *avg=s/n;
    for(s=0,i=0;i<n;i++)
        s+=pow(X[i]-*avg,2);
    *sig=sqrt(s/(n-1));
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int a,s,i,g;
    double A[100];
    printf("input class number: ");
    scanf("%d",&a);
    printf("\n");
    
    for(s=0,i=0;i<a;i++)
       printf("class%d_stu[%2d]: \n",a,i);
       scanf("%d",g);
    
    
    
    
    
    
    
    
    system("pause");
    return(0);
}
