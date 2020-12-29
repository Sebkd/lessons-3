# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func(*args):
    my_calc = list(args).copy()
    my_calc.sort()
    x_number = my_calc.pop()
    y_number = my_calc.pop()
    return (x_number ** y_number)

def my_func_two (*args):
    my_calc = list(args).copy()
    my_calc.sort()
    x_number = my_calc.pop()
    y_number = my_calc.pop()
    revers_x = 1 / x_number
    for count in range(1, abs(y_number)):
        revers_x = revers_x * (1 / x_number)
    return revers_x

while True:
    try:
        in_data = list(map(int, input('Введите через пробел дав числа: X положительное число'
                                        ', а Y второе целое отрицательное\n').split()))
        print(f'Результат возведения числа X в степень Y равен {my_func(in_data[0], in_data[1])}')
        print(f'Результат возведения числа X в степень Y равен {my_func_two(in_data[0], in_data[1])}')
        break
    except IndexError:
        print('Вы ввели меньше 2, попробуйте еще')
        continue
    except ValueError:
        print('Вы ввели не числа, попробуйте еще')
        continue
    except ZeroDivisionError:
        print('Одно из чисел равно 0, попробуйте еще')
        continue