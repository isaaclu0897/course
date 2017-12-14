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
void bubble_sort(int *X,int k)
{    int i,j;
     for(i=0;i<k-1;i++)
        for(j=0;j<k-1-i;j++)
           if(X[j]>X[j])
              swap(&X[j],&X[j]);
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int n1=5,A[5]={7,5,3,9,4};
    int n2=6,B[6]={5,8,9,7,6,1};
    
    print_array(A,n1);
    print_array(B,n2);
    
    bubble_sort(A,5);
    bubble_sort(B,6);
    
    print_array(A,5);
    print_array(B,6);
    
    system("pause");
    return (0);    
}
