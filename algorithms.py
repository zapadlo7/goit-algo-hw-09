inf = float('inf')
coins = [50, 25, 10, 5, 2, 1]
# coins = [4, 3, 1]


def find_coins_greedy(amount):
    coin_count = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            coin_count[coin] = count

    return coin_count


def find_min_coins(amount):
    min_coins = [inf] * (amount + 1)
    min_coins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[amount] == inf:
        return {}

    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        for coin in coins:
            if remaining_amount - coin >= 0 and min_coins[remaining_amount] == min_coins[remaining_amount - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                remaining_amount -= coin
                break

    return result


if __name__ == "__main__":
    print("greedy(213):", find_coins_greedy(213))
    print("dynamic(213):", find_min_coins(213))