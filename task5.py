# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
# чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
exit_key = False

def my_func_summ(*args):
    input_data = args[0]
    sum_data = 0
    global exit_key
    for index in input_data:
        try:
            if 'Q' in index:
                exit_key = True
                return sum_data
            sum_data += int(index)
        except ValueError:
            continue
    return sum_data


save_memory = 0
while exit_key == False:
    in_data = input('Введите через пробел любые числа или введите Q для выхода\n').split(' ')
    save_memory += my_func_summ(in_data)
    print(f'Сумма чисел равна {save_memory}')
    continue
print('Конец программы')
