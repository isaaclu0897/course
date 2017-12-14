# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

int main (){
	FILE *fp_r, *fp_w;
	char s[150];
	int i;
	char filename[50];

	// 為了避免檔案存在，先刷新
	if((fp_r=freopen("HW9_104306033_output.txt","r", stdin)) != NULL){
		printf("file already exist, so i clear, frist\n");
		unlink("HW9_104306033_output.txt");
		fclose(fp_r);
	}	
	for(i=1; i<=20;i++){
		sprintf(filename, "%d.txt", i); 
		/*
		   卡在這裡，因為python 裡面只要 filename = "{}.txt".format(i) 就好，想超久
		   原本想利用之前教的程式hw9-x.c去做匹配一直出問題，後來找到這個，及類似python寫法
		 */
		fp_r = freopen(filename, "r", stdin);
		fp_w = freopen("HW9_104306033_output.txt", "a", stdout);
		while(fgets(s, 150, fp_r)){
			printf("%s", s);
		}
		fclose(fp_r);
		fclose(fp_w);
	}
	return(0);
}
/* 上次的作業，打到一半放棄
int replace(char* str, char* pattern, char* rplc){
	int head, len=4, count, counter=0;
	int i, j, k, a;
	char rplc_obj[100];
	for(head=0;head+len<strlen(str);head++){
		i = head;
		j = len;
		k = 0;
		count=0;
		while(1){
			// 當成功打印 "pattern的長度" 次後，表示成功找出關鍵字
			if(count == strlen(pattern)){
				// printf("%c%s\n", str[i-5], pattern);
				str[i-5] = rplc[0];
				// printf("%c%s\n", str[i-5], pattern);
				for(a=0; a<=len+1; a++){
					rplc_obj[a] = str[i-5];
					i++;
				}
				counter++;
				break;
			}
			// 比對此字元是否與關鍵字元相同，若相同繼續比對
			if(str[i] == pattern[k]){
				i++;
				k++;
				count++;
			}
			else break;
		}
	}
	return rplc_obj[0]; // 這邊就是有問題！！！！沒辦法打印一整個取代後的物件QQ

}
*/
