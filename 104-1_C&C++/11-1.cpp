#include <stdio.h>
#include <stdlib.h>
    int ID[5]={1,3,6,7,9};
    int CH[5]={70,80,90,65,55};
    int EN[5]={20,50,85,45,80};
    double AVG[5];
    int n=5,i;
///////////////////////////////////////////////////////////////////////////////
void swap_i(int *a,int *b)
{   int tmp=*a;
    *a=*b;
    *b=tmp;
}
void swap_d (double *a,double *b)
{   double tmp=*a;
    *a=*b;
    *b=tmp; 
}
void bubble_sort_dec(int *ID,int *CH,int *EN,double *AVG,int n)
{    int i,j;
     for(i=0;i<n-1;i++)
        for(j=0;j<n-1-i;j++)
           if(AVG[j]<AVG[j+1])
           {   swap_i (&ID[j],&ID[j+1]);
               swap_i (&CH[j],&CH[j+1]);
               swap_i (&EN[j],&EN[j+1]);
               swap_d (&AVG[j],&AVG[j+1]);
           }
}
void print_array(int *ID,int *CH,int *EN,double *AVG,int n)
{   int i;
    printf(" id ch en avg \n");
    printf("--------------\n");
    for(i=0;i<n;i++)
       printf(" %2d %3d %3d %5.1f\n",ID[i],CH[i],EN[i],AVG[i]);
}
///////////////////////////////////////////////////////////////////////////////
int main()
{   for(i=0;i<n;i++)
       AVG[i]=0.5*(CH[i]+EN[i]);
    bubble_sort_dec(ID,CH,EN,AVG,n);
    print_array(ID,CH,EN,AVG,n);
    
    system("pause");
    return(0);
}
////////////////////////////////////////////////////////////////////////////////
