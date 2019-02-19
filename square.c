#include<stdio.h>
    int main(void)
    {
    int numRows=4;
    int numCols=5;
    int toPrint=0;
    scanf("%d",&numRows);
    scanf("%d",&numCols);
    int value = 1;
    for (int i = 0; i < numCols;i++) {
      for (int j = 0; j < numRows;j++) {

          if (value<10)
          {
          printf("%d", value);
           if (toPrint){
            value=toPrint+1;
          }
          else{
              value++;
          }
          }
          else{
          toPrint=value;
          printf("%d", value/10);
          value=value%10;
          }
      }
      printf("\n");
    }
  }