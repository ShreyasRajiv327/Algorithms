#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1=0
    for i in range(0,n):
        for k in range(0,n):
            if i==k:
                d1=d1+arr[i][k]
    print(d1)
    i=0
    j=n-1
    d2=0
    while(i!=n and j!=-1):
        d2=d2+arr[i][j]
        i=i+1
        j=j-1
    print(d2)
    ab=d1-d2
    ret=abs(ab)
    return ret
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()