#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{   int a=1,b=50,sol=33,i=1,ans;
    printf("input 1~50 int: ");
    scanf("%d",&ans);
    while(ans!=sol)
    {   if(ans>sol)
           printf("<%2dth> too big  ! and try: \n",i);
        else
           printf("<%2dth> too small! and try: \n",i);
        scanf("%d",&ans);   
        i++;   
    }
    printf("u win");
    
    system("pause");
    return(0);
}
 
