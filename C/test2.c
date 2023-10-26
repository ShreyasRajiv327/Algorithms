#include <stdio.h>

int Q(int n) {
    if (n == 1) {
        return 1;
    } else {
       int  a=(n - 1) + 2 * n - 1;
       printf("\nhii:%d",a);
       printf("\n");
       return Q(n - 1) + 2 * n - 1;
    }
}

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    int result = Q(n);
    printf("Q(%d) = %d\n", n, result);

    return 0;
}
