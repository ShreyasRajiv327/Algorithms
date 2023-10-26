def minimumcoins(coins,amt):
    re=amt
    count=0
    for coin in coins:
        if(amt%coin)==0:
            while coin<=re:
                re=re-coin
                count=count+1