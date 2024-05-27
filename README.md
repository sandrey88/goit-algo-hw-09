# goit-algo-hw-09
Greedy algorithm and dynamic programming

**Порівняння ефективності Жадібного алгоритму та алгоритму Динамічного програмування**
======================================================================================

**Тест 1**
-------------------------------------
***Жадібний алгоритм***
Введіть суму для видачі решти: 113
Номінал монет та їх кількість для видачі решти: {50: 2, 10: 1, 2: 1, 1: 1}
Час виконання жадібного алгоритму: 0.00001121 секунд

***Динамічне програмування***
Введіть суму для видачі решти: 113
Номінал монет та їх кількість для видачі решти: {1: 1, 2: 1, 10: 1, 50: 2}
Час виконання алгоритму динамічного програмування: 0.00009894 секунд

**Тест 2**
-------------------------------------
***Жадібний алгоритм***
Введіть суму для видачі решти: 24222
Номінал монет та їх кількість для видачі решти: {50: 484, 10: 2, 2: 1}
Час виконання жадібного алгоритму: 0.00012898 секунд

***Динамічне програмування***
Введіть суму для видачі решти: 24222
Номінал монет та їх кількість для видачі решти: {2: 1, 10: 2, 50: 484}
Час виконання алгоритму динамічного програмування: 0.03084898 секунд

**Тест 3**
-------------------------------------
Введіть суму для видачі решти: 819191
Номінал монет та їх кількість для видачі решти: {50: 16383, 25: 1, 10: 1, 5: 1, 1: 1}
Час виконання жадібного алгоритму: 0.01488423 секунд

Введіть суму для видачі решти: 819191
Номінал монет та їх кількість для видачі решти: {1: 1, 5: 1, 10: 1, 25: 1, 50: 16383}
Час виконання алгоритму динамічного програмування: 0.97345924 секунд


*************************************
**Висновки**
-------------------------------------

1. Результати всіх трьох наведених вище тестів показують, що швидкодія Жадібного алгоритму в рази вища ніж алгоритму Динамічного програмування. Це особливо помітно на великих сумах решти.

2. Для набору монет [50, 25, 10, 5, 2, 1] обидва алгоритми дають оптимальні результати (мінімальну кількість монет для видачі решти) для всіх тестів.

3. Для практичного застосування, коли потрібно швидко знайти кількість монет (при наборі монет [50, 25, 10, 5, 2, 1]) для видачі решти, жадібний алгоритм є більш підходящим через його швидкість і простоту реалізації.