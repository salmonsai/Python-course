# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.

item = ['rub', 'usd', 'eur', 'chf', 'gbp', 'cny']
rub_rate = [1, 0.0131, 0.0115, 0.0121, 0.0097, 0.0836]


while True:
    target_currency = input(f'Выберите валюту из: {item}')
    print(f'Вы ввели {target_currency}')
    currency_result = 0
    target_currency_amount = input('Введите число: ')

    if target_currency_amount == '':
        print('Вы ввели пустое поле. Введите число.')
    else:
        try:
            target_currency_amount = int(target_currency_amount)
            if target_currency_amount >= 0:
                for i in range(len(item)):
                    if item[i] == target_currency:
                        currency_result = target_currency_amount * rub_rate[i]
                        print(f'Конвертированная сумма в {item[i]} = {currency_result} {item[i]}')
                    else:
                        None
            else:
                print('Введите положительное число.')

        except ValueError:
            print('Вы ввели не число. Введите число.')