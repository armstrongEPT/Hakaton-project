

def password():
    file = open(r"C:/Users/Volch/OneDrive/Рабочий стол/pythonProject3/Date/prepod.txt", 'r', encoding='utf-8')
    prep = file.readlines()
    file.close()
    c = 0
    while True:
        vvod = input('Введите пароль: ')
        for i in prep:
            inf_prep = i.split()
            if vvod == inf_prep[4]:
                print('Ok')
                c += 1
                break
        else:
            print('Повторите ввод')
        if c == 1:
            break


def prepod():
    file = open(r"C:/Users/Volch/OneDrive/Рабочий стол/pythonProject3/Date/prepod.txt", 'r', encoding='utf-8')
    prep = file.readlines()
    file.close()
    c = 0
    while True:
        vvod = input('Введите фамилию: ')
        for i in prep:
            inf_prep= i.split()
            if vvod == inf_prep[1]:
                c += 1
                break
        else:
            print('Повторите ввод')
        if c == 1:
            break

