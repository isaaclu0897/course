#include <stdio.h>
#include <stdlib.h>
int main( )
{
    float a=-12345.12;
    double b=-123456789.123456789;
    
    printf("<%f>\n",a);
    printf("<%025f>\n",a);
    printf("<%25.10f>\n",a);;
    printf("<%-25.10f>\n",a);
    printf("<%+25.10f>\n",a);
    printf("<%025.10f>\n\n",a);
    
    printf("<%lf>\n",b);
    printf("<%025lf>\n",b);
    printf("<%25.10lf>\n",b);
    printf("<%-25.10lf>\n",b);
    printf("<%+25.10lf>\n",b);
    printf("<%025.10lf>\n\n",b);
    
    printf("<%e>\n",a);
    printf("<%025e>\n",a);
    printf("<%25.10e>\n",a);
    printf("<%-25.10e>\n",a);
    printf("<%+25.10e>\n",a);
    printf("<%025.10e>\n\n",a);
    
    printf("<%e>\n",b);
    printf("<%025e>\n",b);
    printf("<%25.10e>\n",b);
    printf("<%-25.10e>\n",b);
    printf("<%+25.10e>\n",b);
    printf("<%025.10e>\n",b);
    system("pause");
    return (0);
}
