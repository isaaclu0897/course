
// 程式碼：
# include <stdio.h>
# include <stdlib.h>

//利用遞迴寫出


float pow(float base, int power)
{ 
    if (power == 0) //當次方等於0的時候
        return 1;
    if (power == 1) //當次方等於1的時候，並且有最後回傳結果得功能
        return base;
    return base * pow(base, power-1); //當次方不等於1時，來到這裡乘上底數，直到次方等於1，跳出方程式。
}

int main(void)
{     double ans1, ans2, ans3;
      float a[2] = {2.5, 4};
      int b[3] = {0, 1, 3};

      ans1 = pow(a[0], b[0]);
      ans2 = pow(a[0], b[2]);
      ans3 = pow(a[1], b[1]);

      printf("%.2f ** %d = %.2lf\n", a[0], b[0], ans1);
      printf("%.2f ** %d = %.4lf\n", a[0], b[2], ans2);
      printf("%.2f ** %d = %.2lf\n", a[1], b[1], ans3);

      return 0;
}
/*
結果：
2.50 ** 0 = 1.00
2.50 ** 3 = 15.6250
4.00 ** 1 = 4.00
*/
