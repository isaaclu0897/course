#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char y2n(int y)
{   int n;
    if((y%4==0&&y%100!=0)||(y%400==0&&4000!=0)) 
       n=1;
    else  
       n=0;
    return(n);
}



//..............................................................................
int main()
{   int y;
    char n;
    
    printf("keyin yours years(number): ");
    scanf("%c",&y);
    
    n=y2n(y);
    switch(n)
    {   case 1 :printf("com\n");break;
        case 0 :printf("leep\n");break;
        default:printf("error");
    }
        
    system("pause");
    return (0);
}
