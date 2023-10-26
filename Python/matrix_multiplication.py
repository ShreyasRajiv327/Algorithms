def multiply(matrix1, matrix2, matrixSizeRows1, matrixSizeColumns1, matrixSizeRows2, matrixSizeColumns2):
    resultantMatrix = []  # Initialize an empty matrix to store the result.
    countAdd = 0  # Initialize a counter for addition operations.
    countMultiply = 0  # Initialize a counter for multiplication operations.
    
    for i in range(matrixSizeRows1):
        resultantRow = []  # Initialize a row in the result matrix.
        for j in range(matrixSizeColumns2):
            dot_product = 0  # Initialize the dot product for the current cell in the result matrix.
            
            # Compute the dot product of corresponding elements in matrix1 and matrix2.
            for k in range(matrixSizeColumns1):
                dot_product += matrix1[i][k] * matrix2[k][j]
                countMultiply += 1  # Increment the multiplication counter.
                countAdd += 1  # Increment the addition counter.
            
            countAdd -= 1  # Decrement the addition counter by 1 to account for the last addition.
            resultantRow.append(dot_product)  # Append the dot product to the current row in the result matrix.
        
        resultantMatrix.append(resultantRow)  # Append the current row to the result matrix.
    
    # Print the resulting matrix.
    for row in resultantMatrix:
        print(' '.join(map(str, row)))
    
    # Print the counts of multiplications and additions.
    print(countMultiply, countAdd)

# Read the dimensions and elements of the first matrix.
MatrixSize1 = list(map(int, input("").split()))
matrixSizeRows1 = MatrixSize1[0]
matrixSizeColumns1 = MatrixSize1[1]
matrix1 = []

for i in range(matrixSizeRows1):
    row1 = list(map(int, input().split()))
    matrix1.append(row1)

# Read the dimensions and elements of the second matrix.
MatrixSize2 = list(map(int, input("").split()))
matrixSizeRows2 = MatrixSize2[0]
matrixSizeColumns2 = MatrixSize2[1]
matrix2 = []

for i in range(matrixSizeRows2):
    row2 = list(map(int, input().split()))
    matrix2.append(row2)

# Check if the matrices can be multiplied (number of columns in the first matrix equals the number of rows in the second matrix).
if matrixSizeColumns1 != matrixSizeRows2:
    print("-1")
else:
    # Call the multiply function with the two matrices and their dimensions.
    multiply(matrix1, matrix2, matrixSizeRows1, matrixSizeColumns1, matrixSizeRows2, matrixSizeColumns2)
