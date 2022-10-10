
def currency(target_currency_amount, item, rub_rate):

    currency_result = 0
    for i in range(len(item)):
        currency_result = target_currency_amount * rub_rate[i]
        print(f'Конвертированная сумма в {item[i]} = {currency_result} {item[i]}')


def target():
    target_currency_amount = input('Введите число: ')

    if target_currency_amount == '':
        print('Вы ввели пустое поле. Введите число.')
        return None
    else:
        try:
            target_currency_amount = int(target_currency_amount)
            if target_currency_amount >= 0:
                return target_currency_amount
            else:
                print('Введите положительное число.')
                return None

        except ValueError:
            print('Вы ввели не число. Введите число.')
            return None


item = ['rub', 'usd', 'eur', 'chf', 'gbp', 'cny']
rub_rate = [1, 0.0131, 0.0115, 0.0121, 0.0097, 0.0836]

target_currency = item[0]
print(f'Вы ввели {target_currency}')

while True:
    result = target()
    if result is not None:
        currency(result, item, rub_rate)


