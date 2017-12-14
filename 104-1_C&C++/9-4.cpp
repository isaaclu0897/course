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
{   int n1=3,n2=5,i;
    double A[3]={50,60,70},avgA,sigA,s;
    double B[5]={50,60,70,80,90},avgB,sigB;
    
    avg_sig(A,n1,&avgA,&sigA);
    avg_sig(B,n2,&avgB,&sigB);
    printf("It is avgA   %f\nIt is sigmaA %f\n",avgA,sigA);
    printf("It is avgB   %f\nIt is sigmaB %f\n",avgB,sigB);
    
    system("pause");
    return(0);
}
