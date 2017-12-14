#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{   FILE *inf,*outf;
    int a,b,sum,pro;
    
    inf=fopen("D:\\a.txt","r");
    if((inf=fopen("D:\\b.txt","w"))==NULL)
    {   printf("error");
        system ("pause");
    }
    outf=fopen("D:\\b.txt","w");
    if((outf=fopen("D:\\b.txt","w"))==NULL)
    {   printf("error");
        system ("pause");
    }
    while(!feof(inf))
    {   fscanf(inf,"%d %d",&a,&b);
        sum=a+b;
        pro=a*b;
        fprintf(outf,"%d %d\n",sum,pro);
    }
    fclose(inf);
    fclose(outf);
    
    
}
