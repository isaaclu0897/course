#include <stdio.h>
#include <stdlib.h>
int P1b(int b)
{   int p=1,i;
    
    for(i=1;i<=b;i++)
        p*=i;
    
    return(p);
}
int Cmn(int m,int n)
{   return(P1b(m)/(P1b(n)*P1b(m-n)));
}
////////////////////////////////////////////////////////////////////////////////
int main( )
{   int c;
    
    c=Cmn(5,2);
    printf("%d",c);
    
    system("pause");
    return(0);
}

