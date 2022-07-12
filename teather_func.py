import  json
import register_students

def check(surname):
    with open('Date/data_file.json') as f:
        file_ = json.load(f)

    for key, value in file_[surname].items():
        print(key, value[2])
    nomer_zadahi = input('Введите номер задачи на которую хотите проверить')
    print('Ответ на задачу ', file_[surname][nomer_zadahi][0])
    file_[surname][nomer_zadahi][1] = input('Дате оценку задания')

    with open("Date/data_file.json", "w") as write_file:
        json.dump(file_, write_file)


def add_qustions():
    with open('Date/data_file.json') as f:
        file_ = json.load(f)

    surname = register_students.surname()
    list_ = list(file_[surname].keys())
    end_key = str(1+int(list_[-1]))
    qustion = input('Введите задание: ')
    file_[surname][end_key] = ['Нет', 'Нет', qustion]

    with open("Date/data_file.json", "w") as write_file:
        json.dump(file_, write_file)










if __name__ == "__main__":
    # with open('Date/data_file.json') as f:
    #     file_ = json.load(f)
    #     print(file_)
    # check(input('Введите фамилию студента, для проверки'))
    add_qustions()