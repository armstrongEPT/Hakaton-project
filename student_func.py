import json

def Answer (surname):

    with open('Date/data_file.json') as f:
        file_ = json.load(f)
        for key, value in file_[surname].items():
            print(key, value[2])
        nomer_zadahi = input('Введите номер задачи на которую дадите ответ')
        print('Ответ на задачу ', file_[surname][nomer_zadahi][0])
        otvet = input('ответ')
        file_[surname][nomer_zadahi][0] = otvet

    with open("Date/data_file.json", "w") as write_file:
        json.dump(file_, write_file)


def Find_rating (surname):
    with open('Date/data_file.json') as f:
        file_ = json.load(f)
        for key, value in file_[surname].items():
            print(key, value[2])
        nomer_zadahi = input('Введите номер задачи на которую хотите узнать оценку')
        print('Оценка за задачу ', file_[surname][nomer_zadahi][1])

def Average_score (surname):
    averege = 0
    count = 0
    with open('Date/data_file.json') as f:
        file_ = json.load(f)
    for key, value in file_[surname].items():
        if value[1].isdigit():
            count += 1
            averege += int(value[0])
            print(value[0])
    if count == 0:
        print("Ваши задания еще не проверены")
    else:
        print(f"По {count} заданиям ваш средний бал {averege/count}")



if __name__ == "__main__":
    with open('Date/data_file.json') as f:
        file_ = json.load(f)
        print(file_)
    #Answer(input ('Введите фамилию'))
    Find_rating (input('Введите фамилию'))
    #Average_score (input('Введите фамилию'))
