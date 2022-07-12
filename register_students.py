import json


def choice():
    while True:
        main_key = input('''1 Преподаватель: 
2 Студент: 
Выберите цифру: ''')
        if not main_key.isdigit():
            print ('Повторите')
        elif main_key == '1' or main_key == '2':
            break
    return main_key


def surname():
    c = 0
    with open('Date/login_pass_student.json', 'r') as a:
        login_pass_student_ = json.load(a)
    while True:
        sur = input('Введите фамилию: ')
        for key in login_pass_student_:
            if sur == key:
                print('OK')
                c += 1
                break
        else:
            print('Фамилия не найдена')
        if c == 1:
            break
    return sur


def password(name):

    with open('Date/login_pass_student.json') as a:
        login_pass_student_ = json.load(a)

    while True:
        sur = input('Введите пароль: ')
        if sur == login_pass_student_[name]:
            print('Пароль введен успешно')
            break
        else:
            print('Пароль не верен')








