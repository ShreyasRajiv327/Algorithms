#include <stdio.h>

int recursiveSum(int n, int i) {
    if (i > n) {
        return 0;
    }
    return i * i + recursiveSum(n, i + 1);
}

int main() {
    int n; // Input value of n
    printf("Enter a positive integer n: ");
    scanf("%d", &n);

    int result = recursiveSum(n, 1);
    printf("The sum is: %d\n", result);

    return 0;
}
