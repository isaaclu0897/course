#include <stdio.h>
#include <stdlib.h>
int main( )
{
    int x=3,y=5,z,
        a=3,b=5,c,
        f=3,g=5,h;
    
    //x++;
    //上列可輸入X++或++X，但X++為後處理，而++X 為前處理 
  
    printf("x=%d y=%d r=0\na=%d b=%d c=0\nf=%d g=%d h=0\n\n",x,y,a,b,f,g);
    z=x*(y++);
    printf("x=%d y=%d z=%d\n\n",x,y,z);
    c=a*(++b);
    printf("a=%d b=%d c=%d\n\n",a,b,c);
    h=(f++)+(++g);
    printf("f=%d g=%d h=%d\n\n",f,g,h);
   
    system("pause");
    return(0);
}
/*compare
  1.r=x*(y++)
  2.r=x*(++y)
  說明
  1.為x與y相乘，最後y才變成y+1            Mathematical:r=x*y+1 
  2.y先變成y+1,然後在x與y相乘             Mathematical:r=x*(y+1)
*/
