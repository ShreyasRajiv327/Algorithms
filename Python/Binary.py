import random
import time
size = int(input("Enter the size of the list: "))
min_value = int(input("Enter the minimum value for random numbers: "))
max_value = int(input("Enter the maximum value for random numbers: "))

array = [random.randint(min_value, max_value) for i in range(0,size)]
array.sort()

def binary_search(ele):
    c = 0
    start = 0
    end = size
    mid = size // 2
    
    if array[mid] == ele:
        print(f"\nElement found at {mid} position")
    else:
        if ele > mid:
            start = mid + 1
        else:
            end = mid
        for start in range(start, end):
            if array[start] == ele:
                print(f"\nElement found at",start,"position")
                c = 1
                break
            else:
                c = 0
        if c == 0:
            print("\nElement not found")

def main():
    if len(array)==0:
        print("\nLength of array is null, No elements in it")
    else:
        array.sort()
        ele = int(input("\nEnter element to be searched: "))
        binary_search(ele)
        
main()
