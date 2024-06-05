import timeit

from algorithms import find_coins_greedy, find_min_coins


amount_values = [10, 100, 1000, 10000]

for amount in amount_values:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
    time_dynamic = timeit.timeit(lambda: find_min_coins(amount), number=100)
    print(f"Для суми {amount}:")
    print("Час виконання жадібного алгоритму:", time_greedy)
    print("Час виконання алгоритму динамічного програмування:", time_dynamic)
    print()