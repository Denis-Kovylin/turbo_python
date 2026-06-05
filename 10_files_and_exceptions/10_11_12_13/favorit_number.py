"""10-11. Улюблене число
Два отдельных скрипта:
первый спрашивает любимое число и сохраняет через json.dump() в файл
второй читает файл через json.load() и выводит сообщение"""

import json

filename = "favorite_number.json"
mess_ask = "What is your favorite number?: "
mess_know = "I know your favorite number! It's "

# user_numb = input(mess_ask)
# with open(filename, 'w') as f:
#     json.dump(user_numb, f)
#
# with open(filename) as f:
#     numb = json.load(f)
#
# print(numb)

"""10-12. Згадати улюблене число
Объединяешь оба скрипта в один. Сначала пробуешь прочитать файл — если есть, выводишь число. 
Если нет (FileNotFoundError) — спрашиваешь и сохраняешь."""
# try:
#     with open(filename) as f:
#         num = json.load(f)
# except FileNotFoundError:
#     user_numb = input(mess_ask)
#     with open(filename, 'w') as f:
#         json.dump(user_numb, f)
#         print(f'Number {user_numb} was saved to {filename}')
# else:
#     print(num)

"""10-13. Перевірка користувача
То же что 10-12 но с именем пользователя. Плюс — если имя уже сохранено, спрашиваешь "это ты?" (yes/no). 
Если нет — просишь ввести новое имя и сохраняешь."""
file_name = "username.json"
mess_welcome_back = "Welcome back"
mess_new_user = "What is your name?: "
mess_confirm = "Is that you? (yes/no): "
mess_greet = "We'll remember you next time!"


def user_check():
    try:
        with open(file_name) as f:
            name = json.load(f)
    except FileNotFoundError:
        user_name = input(mess_new_user)
        with open(file_name, "w") as f:
            json.dump(user_name, f)
            print(mess_greet)
    else:
        with open(file_name) as f:
            print(name)
        user_answer = input(mess_confirm)
        if user_answer == "no":
            user_name = input(mess_new_user)
            with open(file_name, "w") as f:
                json.dump(user_name, f)
                print(mess_greet)
        else:
            print(mess_welcome_back)


user_check()
