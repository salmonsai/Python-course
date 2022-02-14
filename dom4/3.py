# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.

rub_item = 'rub'
rub_rub_rate = 1

usd_item = 'usd'
usd_rub_rate = 0.0131

eur_item = 'eur'
eur_rub_rate = 0.0115

chf_item = 'chf'
chf_rub_rate = 0.0121

gbp_item = 'gbp'
gbp_rub_rate = 0.0097

cny_item = 'cny'
cny_rub_rate = 0.0836

target_currency = rub_item
print(f'Вы ввели {target_currency}')

while True:
    currency_result = 0
    target_currency_amount = input('Введите число: ')

    if target_currency_amount == '':
        print('Вы ввели пустое поле. Введите число.')
    else:
        try:
            target_currency_amount = int(target_currency_amount)
            if target_currency_amount >= 0:
                currency_result = target_currency_amount * eur_rub_rate
                print(f'Конвертированная сумма в EUR = {currency_result} {eur_item}')

                currency_result = target_currency_amount * usd_rub_rate
                print(f'Конвертированная сумма в USD = {currency_result} {usd_item}')

                currency_result = target_currency_amount * chf_rub_rate
                print(f'Конвертированная сумма в CHF =  {currency_result} {chf_item}')

                currency_result = target_currency_amount * gbp_rub_rate
                print(f'Конвертированная сумма в GBP = {currency_result} {gbp_item}')

                currency_result = target_currency_amount * cny_rub_rate
                print(f'Конвертированная сумма в CNY = {currency_result} {cny_item}')
            else:
                print('Введите положительное число.')

        except ValueError:
            print('Вы ввели не число. Введите число.')


