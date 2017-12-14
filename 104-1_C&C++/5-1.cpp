#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main( )
{   int s,count=0;//%d
    char g,sex;//%c
    
    again1://新增1 
    printf("keyin yours sex{M/F}: ");
    scanf("%c",&sex);
    sex=toupper(sex);//新增3 另外還要 #include <ctype.h> 
    fflush(stdin);//新增2.clear key board buffer
    if(sex!='M'&&sex!='F')//新增1 
    {   printf("yours input is error\n");
        goto again1;
    }
    else 
       again2:
       printf("score{0~100}: ");
       scanf("%d",&s);
       if(s<0||s>100)
       {   count++;
           printf("your count is %d\n",count);
           if(count>=3)
           {   printf("yours input is error,and fuck you!Bye!!!\n");
               system("pause");
               return(0);
           }
           else
               goto again2;    
       }
       else
          if(sex=='M')
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
