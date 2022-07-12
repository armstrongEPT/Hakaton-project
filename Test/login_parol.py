import json

data = {
"Петров":'0000',
"Иванов":'1111',
"Сергеев":'2222',
"Васильев":'3333'
}

with open("../Date/login_pass_student.json", "w") as write_file:
    json.dump(data, write_file)