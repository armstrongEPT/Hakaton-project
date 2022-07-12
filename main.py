import student_func
import register_students
import register_teather
import teather_func


main_key = register_students.choice()
if main_key == '1':
    register_teather.prepod()
    register_teather.password()
    choice = ''
    while choice!= '3':
        choice = input(
            'Выберите действие\n'
            '1 Проверять задания\n'
            '2 Добавить задание\n'
            '3 Для выхода\n'
        )
        if choice == '1':
            teather_func.check(input('Введите фамилию студента: '))
        elif choice == '2':
            teather_func.add_qustions()
        else:
            print('Не верный ввод, повторите\n')

else:
    surname = register_students.surname()
    register_students.password(surname)
    choice = ''
    while choice != '4':
        choice = input('Выберите действие\n'
            '1 Решать задания\n'
            '2 Узнать оценку за задание\n'
            '3 Узнать средний бал\n'
            '4 Для выхода\n'
        )
        if choice == '1':
            student_func.Answer(surname)
        elif choice == '2':
            student_func.Find_rating(surname)
        elif choice == '3':
            student_func.Average_score(surname)
        else:
            print('Не верный ввод, повторите\n')




