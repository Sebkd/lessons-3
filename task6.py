# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(*args):
    local_string = args[0].split()
    my_list = []
    my_str = ''
    for index in local_string:
        my_list.append(index.capitalize())
        my_str += my_list.pop() + (' ' if len(local_string) > 1 else '')
    return my_str

def int_func_two(*args):
    local_string = args[0].split()
    my_list = []
    for index in local_string:
        my_list.append(index.capitalize())
    return ' '.join(my_list)

def int_func_three(text):
    return text.title()

text = 'text'
print(f'{text} до преобразования')
print(f'{int_func(text)} после вызова функции')
print(f'{int_func_two(text)} после вызова функции two')
print(f'{int_func_three(text)} после вызова функции three')
text = 'text is text'
print(f'{text} до преобразования')
print(f'{int_func(text).rstrip()} после вызова функции')
print(f'{int_func_two(text)} после вызова функции two')
print(f'{int_func_three(text)} после вызова функции three')