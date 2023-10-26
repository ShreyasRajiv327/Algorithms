import random
import time
size = int(input("Enter the size of the list: "))
min_value = int(input("Enter the minimum value for random numbers: "))
max_value = int(input("Enter the maximum value for random numbers: "))

array = [random.randint(min_value, max_value) for i in range(0,size)]


def linear_search(ele):
    k = 0
    for j in range(size):
        if array[j] == ele:
            print(f"\nElement {ele} is in the position: {j}")
            k = 1
            break
        else:
            k = 0
    if k == 0:
        print("\nElement not found")

def main():
    if len(array)==0:
        print("\nLength of array is null, No elements in it")
    else:
         array.sort()
         ele = int(input("\nEnter element to be searched: "))
         start = time.perf_counter()
         linear_search(ele)
         end = time.perf_counter()
         elapsed_time_ms = (end - start) * 1000  
         print(elapsed_time_ms)
main()
