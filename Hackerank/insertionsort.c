#include <stdio.h>

int main() {
    int n, i, j, temp, comp = 0, move = 0;
    scanf("%d", &n);

    if (n == 0) {
        printf("-1");
        return 0;
    }

    int array[n];

    for (i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    if (n == 1) {
        printf("0\n0\n%d\n", array[0]);
        return 0;
    }

    for (i = 1; i <= n - 1; i++) {
        temp = array[i];
        j = i - 1;
        comp++;
        while (j >= 0 && array[j] > temp) {
            if (j == 0) {
                comp--;
            }
            comp++;
            move++;
            array[j + 1] = array[j];
            j = j - 1;
        }
        array[j + 1] = temp;
    }

    printf("%d\n", comp);
    printf("%d\n", move);

    for (i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }

    return 0;
}
