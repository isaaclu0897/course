#include <stdio.h>
#include <stdlib.h>
int main( )
{
    int   a=2;
    float b=3.14;
    
    printf("<%d><%d><%d>\n\n",sizeof(int),sizeof(float),sizeof(double));
    printf("<%d><%d>\n\n",sizeof(a),sizeof(b));
    system("pause");
    return(0);
}
