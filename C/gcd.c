#include<stdio.h>
int gcd(int a,int b)
{
  int r;
  int ans;
  if (b==0)
  {
    return a;
  }
  else
  {
    r=a%b;
    a=b;
    b=r;
   ans  = gcd(a,b);
  }
  return ans;

  
}

int main()
{
    int a,b;
    printf("\nEnter 2 numbers to find gcd:");
    scanf("\n%d%d",&a,&b);
    int ans=gcd(a,b);
    printf("\nGCD IS %d",ans);
}