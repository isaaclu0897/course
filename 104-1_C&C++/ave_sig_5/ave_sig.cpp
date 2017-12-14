#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//-------------------------------
void ave_sig(double X[],int n,double *average, double *sigma)
{ int i;
  double s;
  for(s=0,i=0;i<n;i++)
    s+=X[i];
  *average=s/n;
  for(s=0,i=0;i<n;i++)
    s+=pow(X[i]-*average,2);
  *sigma=sqrt(s/(n-1));
}
//-----------------------------------------------
int main() 
{ int nc,ic,n,i;
  double A[100],ave,sig;
  
  printf("class no: ");
  scanf("%d",&nc);
  for(ic=0;ic<nc;ic++)
  { printf("\n");
    printf("%d_th class .. stu no: ",ic+1);  
    scanf("%d",&n);
    for(i=0;i<n;i++)
    { printf("  data[%2d]= ",i+1);  
      scanf("%lf",&A[i]);
    }
    ave_sig(A,n,&ave,&sig);
    printf("  ==> average=%6.2lf  sigma=%6.2lf\n",ave,sig);  
  }
  
  printf("\n\n");
  system("pause");
  return(0);  
}      
