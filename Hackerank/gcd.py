input=list(map(int,input("").split()))
a=input[0]
b=input[1]
if b>a:
    while(a!=0):
        r=b%a
        b=a
        a=r
    print(b)
else:
    while(b!=0):
        r=a%b
        a=b
        b=r
    print(a)