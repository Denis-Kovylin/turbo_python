'''Создай файл learning_python.txt в той же папке где будет твой .py файл. Напиши туда несколько строк.
Потом в коде прочитай этот файл тремя способами:'''
# with open('learning_python.txt') as file_object:
#     print(file_object.read())

# with open('learning_python.txt') as file_object:
#     for line in file_object:
#         print(line)

# with open('learning_python.txt') as file_object:
#     content = file_object.readlines()
# for line in content:
#     print(line)

'''Берёшь тот же файл, читаешь строки и заменяешь слово Python на C через .replace('Python', 'C').
 Выводишь изменённые строки.'''
# with open('learning_python.txt') as file_object:
#     list_of_strings = file_object.readlines()
#
# edited_strings_list = []
# for string in list_of_strings:
#     edited_strings_list.append(string.replace('Python', 'JS'))
#
# for string in edited_strings_list:
#     print(string.strip())

