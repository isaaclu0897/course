#include <stdio.h>
#include <stdlib.h>
int main()
{  
  int av,b,c,d,f;
  printf("Hello\nHow are you?\nI am fine!\nThank,and you?\n");
  printf("keyin av&b&c&d:");
  scanf ("%d%d%d%d",&av,&b,&c,&f);
  d=av*b-c+f;
  printf("%d*%5d-%5d+%5d+++++%5d\n",av,b,c,f,d);
  system("pause");
  return 0;
}
