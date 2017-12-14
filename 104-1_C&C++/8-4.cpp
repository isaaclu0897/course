#include <stdio.h>
#include <stdlib.h>
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int A[3]={11,22,33};
    int i,s;
    
    for(i=0,s=0;i<3;i++)
       s+=A[i];
    
    printf("%d",s);
    
    system("pause");
    return (0);    
}
