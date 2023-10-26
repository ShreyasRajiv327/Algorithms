#include <stdio.h>

void multiply(int matrix1[][100], int matrix2[][100], int matrixSizeRows1, int matrixSizeColumns1, int matrixSizeRows2, int matrixSizeColumns2) {
    int resultantMatrix[100][100];
    int countAdd = 0;
    int countMultiply = 0;

    for (int i = 0; i < matrixSizeRows1; i++) {
        for (int j = 0; j < matrixSizeColumns2; j++) {
            int dot_product = 0;
            for (int k = 0; k < matrixSizeColumns1; k++) {
                dot_product += matrix1[i][k] * matrix2[k][j];
                countMultiply++;
                countAdd++;
            }
            countAdd--;
            resultantMatrix[i][j] = dot_product;
        }
    }

    for (int i = 0; i < matrixSizeRows1; i++) {
        for (int j = 0; j < matrixSizeColumns2; j++) {
            printf("%d", resultantMatrix[i][j]);
            if (j < matrixSizeColumns2 - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }

    printf("%d %d\n", countMultiply, countAdd);
}

int main() {
    int matrixSizeRows1, matrixSizeColumns1;
    scanf("%d %d", &matrixSizeRows1, &matrixSizeColumns1);

    int matrix1[100][100];
    for (int i = 0; i < matrixSizeRows1; i++) {
        for (int j = 0; j < matrixSizeColumns1; j++) {
            scanf("%d", &matrix1[i][j]);
        }
    }

    int matrixSizeRows2, matrixSizeColumns2;
    scanf("%d %d", &matrixSizeRows2, &matrixSizeColumns2);

    int matrix2[100][100];
    for (int i = 0; i < matrixSizeRows2; i++) {
        for (int j = 0; j < matrixSizeColumns2; j++) {
            scanf("%d", &matrix2[i][j]);
        }
    }

    if (matrixSizeColumns1 != matrixSizeRows2) {
        printf("-1\n");
    } else {
        multiply(matrix1, matrix2, matrixSizeRows1, matrixSizeColumns1, matrixSizeRows2, matrixSizeColumns2);
    }

    return 0;
}
