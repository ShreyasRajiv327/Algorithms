L = []

def bubblesort():
    count = 0
    for j in range(len(L)):
        for k in range(len(L) - 1):
            if L[k] > L[k + 1]:
                L[k], L[k + 1] = L[k + 1], L[k]
                count += 1
    print(count)

def main():
    n = int(input("Enter Range"))
    for i in range(n):
        ele = int(input("Enter Value"))
        L.append(ele)
    bubblesort()
    print(L)

main()
