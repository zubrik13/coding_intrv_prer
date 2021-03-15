# greedy algorithm

def coinChange(coins, amount):
    coins = sorted(coins)

    flag = None
    for coin in coins:
        if coin == amount: return coin
        if coin < amount:
            flag = coin
    coins_to_return = amount - flag
    return [flag] + [coinChange(coins, coins_to_return)]




        
coins = [1,2,5]
amount = 11
# coins = [186,419,83,408]
# amount = 6249

result = coinChange(coins, amount)

print(coinChange(coins, amount))




"""
    if amount == 0:
        return amount
    
    coins = sorted(coins)
    
    max_val = max(coins)
    min_val = min(coins)
    
    # amount_to_change = amount
    min_num_coins = 0
    index = len(coins) - 1
    # print(coins[index])
    
    while amount > 0:
        if amount >= max_val:
            amount -= max_val
            min_num_coins += 1
        elif len(coins) == 1:
            return -1
        else:
            max_val = coins[index-1]
            index -= 1
            
    return min_num_coins

"""