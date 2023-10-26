CommonA=[]
CommonB=[]
Common=[]
PrimeA=[]
PrimeB=[]
Final=[]
def commonp(a,b):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            for k in range(1,i+1):
                if i%k==0:
                    count=count+1
            if count==2:
                CommonA.append(i)
            count =0
    print("Factors of:",a,"is:",CommonA)
    count=0
    for i in range(1,b+1):
        if b%i==0:
            for k in range(1,i+1):
                if i%k==0:
                    count=count+1
            if count==2:
                CommonB.append(i)
            count =0
    print("Factors of:",b,"is:",CommonB)
def gcd(a,b):
    for i in range(0,len(CommonA)):
        while(a%CommonA[i]==0):
            a=a/CommonA[i]
            PrimeA.append(CommonA[i])
    print("Prime Factorization of A:",PrimeA)
    for i in range(0,len(CommonB)):
        while(b%CommonB[i]==0):
            b=b/CommonB[i]
            PrimeB.append(CommonB[i])
    print("Prime Factorization of B:",PrimeB)                
    for k in PrimeA:
        if k in PrimeB:
            Final.append(k)
    if len(Final)==0:
        Final.append(1)
    gcd=1
    for k in range(0,len(Final)):
        gcd=gcd*Final[k]
    print("Gcd is ",gcd,"Factorized->",Final)  
def main():
    a=966
    b=434
    commonp(a,b)      
    gcd(a,b)
main()