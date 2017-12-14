#include <stdio.h>
#include <stdlib.h>
void print_array(int *X,int k)
{    int i;
     for(i=0;i<k;i++)
        printf("%d  ",X[i]);
     printf("\n");
}
void swap(int *x,int *y)
{    int tmp;

     tmp=*x;
     *x=*y;
     *y=tmp;
     
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int A[5]={7,5,3,9,4};
    int n=5,i,j;
    
    print_array(A,n);
    
    for(i=0;i<=(n-2);i++)
    {   for(j=0;j<=(n-2);j++)
           if(A[j]>A[j+1])
              swap(&A[j],&A[j+1]);
             
        print_array(A,n);
    }
    system("pause");
    return (0);    
}
