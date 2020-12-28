# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def printing_data_user (**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}; ', end=' ')
printing_data_user(names='John',
                   surnames='Travolta',
                   year_of_birth='1956',
                   city='Passadena',
                   email='travolta_official@mail.us',
                   phone='1-911-911-00-00')

