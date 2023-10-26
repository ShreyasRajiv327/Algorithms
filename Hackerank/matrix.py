def multiplication(matrixr1,matrixc1,matrixr2,matrixc2,matrix1,matrix2):
    add = 0
    multi = 0
    matrix =[]
    for i in range(matrixr1):
        resrow=[]
        for j in range(matrixc2):
            temp=0
            for k in range(matrixc1):
                temp += matrix1[i][k]*matrix2[k][j]
                add += 1
                multi += 1
            add -= 1
            resrow.append(temp)
        matrix.append(resrow)
    for ele in matrix:
        print(" ".join(map(str,ele)))
    print(multi,add)
        

matrixs1=list(map(int,input("").split()))
matrixr1=matrixs1[0]
matrixc1=matrixs1[1]
matrix1=[]
for i in range(matrixr1):
    row=list(map(int,input("").split()))
    matrix1.append(row)
matrixs2=list(map(int,input("").split()))
matrixr2=matrixs2[0]
matrixc2=matrixs2[1]
matrix2=[]
for i in range(matrixr2):
    row=list(map(int,input("").split()))
    matrix2.append(row)
if matrixc1 != matrixr2:
    print("-1")
else:
    multiplication(matrixr1,matrixc1,matrixr2,matrixc2,matrix1,matrix2)
