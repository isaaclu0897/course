
// 第一題

# include <stdio.h>
# include <stdlib.h>

int main(){
    int a=11;

    while(a-->=0){
        int b=10, c=0;
        while(c++<=a){
            printf("/");
        }
        while(b-->=a){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}

// 第二題

# include <stdio.h> 
# include <stdlib.h>

int main(){
    int a=10;

    while(a-->=0){
        int b=0, c=10;
        while(c-->a){ 
            printf("/");
        }
        while(b++<=a){
            printf("*");
        }
        printf("\n");

    }

    return 0;
}
