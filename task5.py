# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
# чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def my_func_summ(*args):
    print(args)
    input_data = list(args).copy()
    print(input_data)
    sum_data = 0
    for index in input_data:
        if 'q' or 'Q' in in_data:
            exit_key = True
            return sum_data
        sum_data += int(index)
    return sum_data


save_memory = 0
exit_key = False
while exit_key == False:
    in_data = input('Введите через пробел любые числа или введите q для выхода\n').split(' ')
    save_memory = save_memory + my_func_summ(in_data)
    print(f'Сумма числе равна {save_memory}')
    continue
print('The end')
