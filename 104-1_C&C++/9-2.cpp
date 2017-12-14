#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int n=5;
double A[5]={50,60,70,80,90},avg,sig;
/////////////////////////////////////////////////////////////////////////////// 
double average( )
{      int i;
       double s;
       
       for(s=0,i=0;i<n;i++)
           s+=A[i];
       return(s/n);
}

double sigma( )
{      int i;
       double s;
       
       for(s=0,i=0;i<n;i++)
           s+=pow(A[i]-avg,2);
       return(sqrt(s/(n-1)));
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int i; 
    
    avg=average();
    sig=sigma();
    
    printf("It is avg %f\nIt is sigma %f\n",avg,sig);
    
    system("pause");
    return(0);
}
