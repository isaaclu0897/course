
#include <stdio.h>

int func(int num) // 檢驗方程
{ 
int i; 
if (num == 2) return 1; // 2必為素數
else
for (i=2; i<=num/2; i++) // num/2 加速算法, num=2程式跑步出來不知為何？
{ 
if ((num % i) == 0) 
return 0; 
} 
return 1; 
}

int main()
{
FILE *f;
int i;
int count_num = 0;
f = freopen(" HW4_1_104306033.txt", "w", stdout);
printf("this is homework4-1 of 104306033\n\n");
for (i=2; i<=10000; i++) //簡驗2到10000, 1不是素數直接跳過
{
if (func(i))
{
printf("%4d\t", i);
count_num++;
if (count_num % 5 == 0) //每5個素數換一行,方便老師閱讀改的：）
printf("\n");
} 
}
printf("\n\nthe number is: %d", count_num);
fclose(stdout);

return 0;
}
