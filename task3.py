# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(*args):
    my_calc = list(args).copy()
    my_calc.sort()
    return (my_calc.pop() + my_calc.pop())

while True:
    try:
        in_data = list(map(float, input('Введите через пробел три числа\n').split()))
        print(f'Сумма наибольших чисел равна {my_func(in_data[0], in_data[1], in_data[2])}')
        break
    except IndexError:
        print('Вы ввели меньше 3, попробуйте еще')
        continue
    except ValueError:
        print('Вы ввели не числа, попробуйте еще')
        continue