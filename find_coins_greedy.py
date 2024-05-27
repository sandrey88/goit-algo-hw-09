import time

# Жадібний алгоритм
def find_coins_greedy(amount):

    start_time = time.time()  # Запис початкового часу (для обчислення часу виконання алгоритму)

    # Номінали монет
    coin_values = [50, 25, 10, 5, 2, 1]

    # Словник для зберігання номіналу монет та їх кількості
    coins = {}
    for coin in coin_values:
        while amount >= coin:
            amount -= coin
            if coin not in coins:
                coins[coin] = 0
            coins[coin] += 1

    end_time = time.time()  # Запис кінцевого часу
    total_time = end_time - start_time  # Обчислення загального часу

    print(f"Номінал монет та їх кількість для видачі решти: {coins}")
    print(f"Час виконання жадібного алгоритму: {total_time:.8f} секунд")
    
    return coins

# Приклад використання
amount = int(input("Введіть суму для видачі решти: "))
# Запуск алгоритму
find_coins_greedy(amount)
