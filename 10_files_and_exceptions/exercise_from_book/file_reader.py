'''Реализация базового ридера текстовых файлов и чтение файла'''
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

'''Построчное чтение файла циклом'''
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line)

'''Создание списка строк при чтении файла. Возможность просматривать их в не блока with'''
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     list_of_lines = file_object.readlines()
# for line in list_of_lines:
#     print(line)

'''Работа с файлом. Перебор списка строк и сохранение в одну строку с стрипом пробелов'''
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     list_of_lines = file_object.readlines()
#
# pi_sting = ''
# for line in list_of_lines:
#     pi_sting += line.strip()
# print(pi_sting)
# print(len(pi_sting))

'''Вивод первых 50 символов числа ПИ слайсом и длинны числа'''
# file_name = 'pi_million.txt'
# with open(file_name) as file_object:
#     list_of_lines = file_object.readlines()
#
# pi_sting = ''
# for line in list_of_lines:
#     pi_sting += line.strip()
# print(f'{pi_sting[:52]}...')
# print(len(pi_sting))

'''Найти свой день рождения в первом миллионе символов числа ПИ'''
# file_name = 'pi_million.txt'
# with open(file_name) as file_object:
#     list_of_lines = file_object.readlines()
#
# pi_string = ''
# for line in list_of_lines:
#     pi_string += line.strip()
#
# birthday = input('Enter your birthday data (mmddyy): ')
# if birthday in pi_string:
#     print('Your birthday appear in first million symbol of number PI')
# else:
#     print('Your birthday does not appear in first million symbol of number PI')