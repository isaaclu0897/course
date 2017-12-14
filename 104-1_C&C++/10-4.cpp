#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{   char sex;
    printf("sex(M/F): ");
    scanf("%c",&sex);
    sex=toupper(sex);
    fflush(stdin);
    while(sex!='M'&&sex!='F')
    {   printf("Error input!\n");
        printf("sex(M/F): ");
        scanf("%c",&sex);
        sex=toupper(sex);
        fflush(stdin);
    }
    
    system("pause");
    return(0);
}
 
