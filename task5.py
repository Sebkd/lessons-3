# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
# чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def my_func_summ (*args):
    for index_number in list(args).copy():
        for i in index_number
        return sum(index_number)

def memory_save_summ (*args):
    pass




save_memory = 0
while True:
    try:
        in_data = list(map(int, input('Введите через пробел любые числа\n').split()))
        save_memory = save_memory + my_func_summ(in_data)
        print(f'Сумма числе равна {save_memory}')
        continue
    # except IndexError:
    #     print('Вы ввели меньше 2, попробуйте еще')
    #     continue
    except ValueError:
        print('Вы ввели не числа, попробуйте еще')
        continue
    # except ZeroDivisionError:
    #     print('Одно из чисел равно 0, попробуйте еще')
    #     continue