#include <stdio.h>
#include <stdlib.h>

int GCD(int a,int b)
{   int r;
    r=a%b;
    while(r!=0)
    {   a=b;
        b=r;
        r=a%b;
    }
    return(b);
}

int LCM(int a,int b)
{   return(a*b/GCD(a,b));
}

int main( )
{   int a,b;
    printf("块ㄢ计眔程そ计㎝程そ计: ");
    scanf("%d %d",&a,&b);
    printf("%d\n",GCD(a,b));
    printf("%d\n",LCM(a,b));
    
   
    system("pause");
    return(0);
}
 
