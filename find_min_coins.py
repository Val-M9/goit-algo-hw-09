import timeit


def find_min_coins(coins, amount):
    coins.sort()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result


coins = [1, 2, 5, 10, 25, 50]
amount = 1619
print(find_min_coins(coins, amount))


work_time = timeit.timeit(lambda: find_min_coins(coins, amount), number=10)
print(f'Execution time: {work_time}')
