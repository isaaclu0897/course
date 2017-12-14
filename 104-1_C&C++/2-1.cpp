#include <stdio.h>
#include <stdlib.h>
int main( )
{
    int a,b;
    
    printf("keyin 2 int: ");
    scanf("%d%d",&a,&b);
    
    printf("<%d><%d>      \n",a,b);
    printf("<%10d><%10d>  \n",a,b);
    printf("<%-10d><%-10d>\n",a,b);
    printf("<%+10d><%+10d>\n",a,b);
    printf("<%010d><%010d>\n",a,b);
    printf("<%010d><%010d>\n",a,b);
    
    printf("\n\n");
    system("pause");
    return (0);
}
