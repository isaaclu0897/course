
# include <stdio.h>
# include <stdlib.h>
// 創建一個good函數(就是第二次作業辣)
int good(char C, int L, int N){
int i=0;
// 波數
while(i++ < N){
int a1 = L, a2 = L;
// 打印 L 行，最後一行 L 字
while(a1-- > 0){
int b = 0, c = L;
while(c-- > a1){
printf("%c", C);
}
printf("\n");
}
// 打印 L - 1 行，第一行 L - 1 字
while(a2-- > 0){
int b = L, c = 0;
while(c++ < a2){
printf("%c", C);
}
if(c != 1) printf("\n");// 這裡要特別處裡，因為我代碼打得不好，兩個波之間會出現空格，所以家這行消掉
}
}
}

int main(){
char a;
int b, c;
printf("input C, L, N :");
scanf("%c %d %d", &a, &b, &c);
good(a, b, c);
return 0;
}
