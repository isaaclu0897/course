#include <stdio.h>
#include <stdlib.h>
typedef struct record
{   int id,ch,en;
    double avg;
    char grade;
    int rank;
}   RECORD;
///////////////////////////////////////////////////////////////////////////////
void bubble_sort_dec(RECORD* ,int );
void ranking(RECORD* ,int );
char grade_f(double );
void print_array(RECORD* ,int );
///////////////////////////////////////////////////////////////////////////////
int main()
{   RECORD B[5]={{22,60,150},{33,70,50},{29,40,60},{36,10,15},{31,80,90}};
    int i,n=5;
    for(i=0;i<n;i++)
    {   B[i].avg=0.5*(B[i].ch+B[i].en);
        B[i].grade=grade_f(B[i].avg);
    }
    bubble_sort_dec(B,n);
    ranking(B,n);
    print_array(B,n);
    
    system("pause");
    return(0);
}
////////////////////////////////////////////////////////////////////////////////
void bubble_sort_dec(RECORD *A,int n)
{   int i,j;
    RECORD tmp;
    for(i=0;i<n;i++)
       for(j=0;j<n-1-i;j++)
          if(A[j].avg<A[j+1].avg)
          {   tmp=A[j];
              A[j]=A[j+1];
              A[j+1]=tmp;
          }
}
void ranking(RECORD *A,int n)
{   int i;
    for(i=0;i<n;i++)
       A[i].rank=i+1;
       
    for(i=1;i<n;i++)
       if(A[i].avg==A[i-1].avg)
          A[i].rank=A[i-1].rank;
}
char grade_f(double s)
{        if(s>=80) return('A');
    else if(s>=70) return('B');
    else if(s>=60) return('C');
    else           return('D');
}
void print_array(RECORD *A,int n)
{   int i;
    printf(" id ch en avg grade rank\n");
    printf("------------------------\n");
    for(i=0;i<n;i++)
       printf(" %2d %3d %3d %5.1f %c %2d\n",A[i].id,A[i].ch,A[i].en,A[i].avg,A[i].grade,A[i].rank);
}



