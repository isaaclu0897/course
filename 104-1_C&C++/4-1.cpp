#include <stdio.h>
#include <stdlib.h>
int main( )
{
    int a;
    printf("keyin one integer: ");
    scanf("%d",&a);
    
    if(a>=0)
       printf("%d>=0",a);
    else
       printf("%d<0",a);
    
    printf("\n\n");
    system("pause");
    return (0);
}
