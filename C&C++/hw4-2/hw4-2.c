
// 老師你i學園上傳的亂數檔只有619行喔～不過輸出輸入都是自動化的應改沒差
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (){
FILE *fp_r, *fp_w;
char s[150];
char t[]="Peter";
int head, len=5, count, counter=0;
int i, j, k;


fp_r = freopen("random_letter.txt","r", stdin);
fp_w = freopen("HW4_2_104306033.txt", "w", stdout);
printf("this is homework4-2 of 104306033\n\n");
//以行讀檔
while(fgets(s, 150, fp_r) != NULL){
//printf("this line is : %s\n",s); //打印本行
//行搜索，可見模，原本像用正則表達式的，可是我看了一星期還是不太會 QQ
for(head=0;head+len<strlen(s);head++){
i = head;
j = len;
k = 0;
count=0;

while(1){
// 當成功打印"t的長度"次後，表示成功找出關鍵字
if(count == strlen(t)){
printf("%cPeter%c\n", s[i-6], s[i]);
counter++; 
break;
}
// 比對此字元是否與關鍵字元相同，若相同繼續比對
if(s[i] == t[k]){
i++;
k++;
count++;
}
else break;
}
}
}
printf("\ntotal find %d of Peter\n", counter);
fclose(fp_r);
fclose(fp_w);
return(0);
}
