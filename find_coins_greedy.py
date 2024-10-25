import timeit


def find_coins_greedy(coins, amount):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        while amount >= coin:
            amount -= coin
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1

    return result


coins = [1, 2, 5, 10, 25, 50]
amount = 1619
print(find_coins_greedy(coins, amount))

work_time = timeit.timeit(lambda: find_coins_greedy(coins, amount), number=10)
print(f'Execution time: {work_time}')
