#include <stdio.h>
#include <stdlib.h>
int main( )
{
    int s;//%d
    char g;//%c
    
    printf("keyin yours score: ");
    scanf("%d",&s);
    
    if     (s>=90) g='A';   
    else if(s>=80) g='B';
    else if(s>=70) g='C';
    else if(s>=60) g='D';
    else           g='E';
    
    printf("yours grade is %c",g);
    printf("\n\n");
    system("pause");
    return (0);
}
