#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double average(double X[],int n)
{   int i;
    double s;
    for(s=0,i=0;i<n;i++)
        s+=X[i];
    return(s/n);
}

double sigma(double X[],int n,double avg)
{   int i;
    double s;
    for(s=0,i=0;i<n;i++)
        s+=pow(X[i]-avg,2);
    return(sqrt(s/(n-1)));
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int n1=3,n2=5,i;
    double A[3]={50,60,70},avgA,sigA,s;
    double B[5]={50,60,70,80,90},avgB,sigB;
    
    avgA=average(A,n1);
    sigA=sigma(A,n1,avgA);
    avgB=average(B,n2);
    sigB=sigma(B,n2,avgB);
    printf("It is avgA   %f\nIt is sigmaA %f\n",avgA,sigA);
    printf("It is avgB   %f\nIt is sigmaB %f\n",avgB,sigB);
    
    system("pause");
    return(0);
}
