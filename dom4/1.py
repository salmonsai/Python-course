# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

usd_item = 'usd'
usd_usd_rate = 1

eur_item = 'eur'
eur_usd_rate = 1.14

target_currency = eur_item
target_currency_amount = int(input('Введите число: '))
currency_result = 0

if target_currency == 'eur':
    print(f'Ты ввёл {eur_item}')
    currency_result = target_currency_amount * eur_usd_rate
    print(f'Конвертированная сумма в USD = {currency_result} {usd_item}')
else:
    print('None')


