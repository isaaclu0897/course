#include <stdio.h>
#include <stdlib.h>
int main( )
{   int s;//%d
    char g,sex;//%c
    
    printf("keyin yours sex: ");
    scanf("%c",&sex);
    printf("keyin yours score: ");
    scanf("%d",&s);
    
    if(sex=='M'||sex=='m')
    {   if     (s>=90) g='A';   
        else if(s>=80) g='B';
        else if(s>=70) g='C';
        else if(s>=60) g='D';
        else           g='E';       
    }
    else
    {   if     (s>=85) g='A';   
        else if(s>=75) g='B';
        else if(s>=65) g='C';
        else if(s>=55) g='D';
        else           g='E';
    }
    
    printf("yours grade is %c\n\n",g);
    
    
    system("pause");
    return (0);
}
