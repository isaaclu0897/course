#include <stdio.h>
#include <stdlib.h>
int main( )
{
    int x=3,y=5,z,
        a=3,b=5,c,
        f=3,g=5,h;
    
    //x++;
    //�W�C�i��JX++��++X�A��X++����B�z�A��++X ���e�B�z 
  
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
  ����
  1.��x�Py�ۭ��A�̫�y�~�ܦ�y+1            Mathematical:r=x*y+1 
  2.y���ܦ�y+1,�M��bx�Py�ۭ�             Mathematical:r=x*(y+1)
*/
