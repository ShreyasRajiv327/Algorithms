#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int r1,c1;
    scanf("\n%d %d",&r1,&c1);
    int i;
    int j;
    int matrix1[r1][c1];
    for(i=0;i<r1;i++)
    {
        for(j=0;j<c1;j++)
        {
            scanf("%d",&matrix1[i][j]);
        }
    }
    int r2,c2;
    scanf("\n%d %d",&r2,&c2);
    int matrix2[r2][c2];
    for(i=0;i<r2;i++)
    {
        for(j=0;j<c2;j++)
        {
            scanf("%d",&matrix2[i][j]);
        }
    }
    if(r1+c1!=r2+c2)
    {
        int del=-1;
        printf("%d",del);
    }
    else
    {
      int matrix3[r2][c2];
      for(i=0;i<r2;i++)
      {
        for(j=0;j<c2;j++)
        {
            matrix3[i][j]=matrix1[i][j]+matrix2[i][j];
        }
      }
        
      for(i=0;i<r2;i++)
      {
        for(j=0;j<c2;j++)
        {
            printf("%d ",matrix3[i][j]);
            
        }
         printf("\n");
      }
     
      int count=0;
      for(i=0;i<r2;i++)
      {
        for(j=0;j<c2;j++)
        {
            count++;
            
        }
      }
        
       printf("%d",count);
        
    }
        
}
