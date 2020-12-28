# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division (var_1, var_2):
    return var_1 / var_2

while True:
    try:
        if input('Выход - Q, \nЛюбая клавиша - продолжить:\n ').upper() == 'Q':
            break
        in_data = list(input('Введите через пробел два числа для деления\n').split())
        print(f'Результат деления первого числа на второе {round(division(float(in_data[0]), float(in_data[1])),2)}')
    except ZeroDivisionError:
            print('Вы ввели 0, попробуйте еще')
            continue
    except ValueError:
            print('Вы ввели не числа, попробуйте еще')
            continue
    except IndexError:
            print('Вы ввели одно число, нужно два, попробуйте еще')
            continue