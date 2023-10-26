
def minCoins(coins, amt) :
    if amt == 0 :
        return 0
    
    Count = 0
    for coin in coins :
        if coin <= amt :
            count = 1 + minCoins(coins, amt - coin)
            if (Count == 0) or (count < Count) :
                Count = count
    
    return Count

n = int(input(""))
delimiter_1 = input("")
coins = list(map(int, input("").split()))
delimiter_2 = input("")
Total = int(input(""))

result = minCoins(coins, Total)
print(result)