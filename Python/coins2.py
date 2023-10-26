def minimumCoins(coins, amt):
    coins.sort(reverse=True)  # Sort the coins in descending order

    coin_count = 0  # Initialize the count of coins used
    remaining_amt = amt  # Initialize the remaining amount to the target amount

    for coin in coins:
        #if(amt%coin==0):
            print("value before while loop",remaining_amt)
            print(coin)
            while coin <= remaining_amt:
                remaining_amt -= coin  # Subtract the coin from the remaining amount
                coin_count += 1  # Increment the coin count
                print("Value after while loop",remaining_amt)
        

    if remaining_amt == 0:
        return coin_count  # If the remaining amount is 0, return the coin count
    else:
        return -1  # If it's not possible to make the amount, return -1

# Example usage:
coins = [9, 6, 5, 1]
amt = 11
result = minimumCoins(coins, amt)

if result != -1:
    print("The minimum number of coins needed is:", result)
else:
    print("It's not possible to make the amount with the given coins.")
