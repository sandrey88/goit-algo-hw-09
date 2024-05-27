import time

# Динамічне програмування
def find_min_coins(amount):
    start_time = time.time()  # Запис початкового часу (для обчислення часу виконання алгоритму)

    # Номінали монет
    coin_values = [50, 25, 10, 5, 2, 1]

    # Масив для зберігання мінімальної кількості монет для кожної суми
    coins = [float('inf')] * (amount + 1)
    coins[0] = 0

    # Масив для зберігання останньої використаної монети для кожної суми
    last_coin = [-1] * (amount + 1)

    for m in range(1, amount + 1):
        for coin in coin_values:
            if m >= coin and coins[m - coin] + 1 < coins[m]:
                coins[m] = coins[m - coin] + 1
                last_coin[m] = coin

    # Словник для зберігання номіналу монет та їх кількості
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        if coin == -1:
            print("Неможливо видати решту за допомогою наявних монет.")
            return {}
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    end_time = time.time()  # Запис кінцевого часу
    total_time = end_time - start_time  # Обчислення загального часу

    # Виведення результату у відсортованому порядку
    sorted_result = dict(sorted(result.items()))

    print(f"Номінал монет та їх кількість для видачі решти: {sorted_result}")
    print(f"Час виконання алгоритму динамічного програмування: {total_time:.8f} секунд")

    return sorted_result

# Приклад використання
amount = int(input("Введіть суму для видачі решти: "))
# Запуск алгоритму
find_min_coins(amount)
