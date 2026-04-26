# Python — While Loop & User Input

---

## 1. Базовая структура while

while условие:  
    # выполняется пока условие True  

цикл крутится до тех пор, пока условие не станет False  

---

## 2. input() — ввод от пользователя

user_input = input('Введи что-нибудь: ') — всегда возвращает строку  
age = int(input('Введи возраст: ')) — конвертировать в int вручную  

проверка до конвертации:

if not user_input.isdigit():  
    print('Только цифры!')  
else:  
    age = int(user_input)  

---

## 3. Флаг для управления циклом

active = True  
while active:  
    user_input = input('Команда: ')  
    if user_input == 'quit':  
        active = False  

использовать флаг вместо break когда нужно завершить цикл из нескольких мест  

---

## 4. while True и break

while True:  
    user_input = input('Команда: ')  
    if user_input == 'quit':  
        break  

break — немедленно выходит из цикла  
использовать когда условие выхода только одно  

---

## 5. continue — пропустить итерацию

while active:  
    user_input = input('Введи число: ')  
    if user_input == '':  
        print('Поле обязательно!')  
        continue  
    if not user_input.isdigit():  
        print('Только цифры!')  
        continue  
    number = int(user_input)  

continue — пропускает остаток итерации и возвращается к условию while  

---

## 6. Итерация списка через while (pop)

items = ['a', 'b', 'c']  
processed = []  

while items:  
    current = items.pop()  
    processed.append(current)  

while items: — цикл крутится пока список не пустой  
pop() — забирает и удаляет последний элемент  

---

## 7. Удаление всех вхождений элемента

my_list = ['a', 'b', 'a', 'c', 'a']  

while 'a' in my_list:  
    my_list.remove('a')  

remove() — удаляет первое вхождение, поэтому нужен while  
(for не подходит — нельзя изменять список во время итерации по нему)  

---

## 8. Сбор данных в словарь через while

responses = {}  
active = True  

while active:  
    name = input('Имя: ')  
    answer = input('Ответ: ')  
    responses[name] = answer  
    again = input('Ещё кто-то? (y/n): ')  
    if again != 'y':  
        active = False  

for name, answer in responses.items():  
    print(f'{name}: {answer}')  

---

## 9. Проверка ввода — типичный паттерн

while True:  
    user_input = input('Введи число: ')  
    if user_input == '':  
        print('Поле не может быть пустым')  
        continue  
    if user_input == 'quit':  
        break  
    if not user_input.isdigit():  
        print('Только цифры')  
        continue  
    number = int(user_input)  
    # обработка числа  
    break  

---

## 10. Частые ошибки

бесконечный цикл — условие никогда не становится False:

# ОПАСНО:
while active:  
    print('бесконечно')  
    # забыли изменить active  

# ПРАВИЛЬНО:
while active:  
    user_input = input('quit для выхода: ')  
    if user_input == 'quit':  
        active = False  

изменение списка во время for-итерации — использовать while:

# НЕПРАВИЛЬНО:
for item in my_list:  
    my_list.remove(item)  # пропустит элементы  

# ПРАВИЛЬНО:
while 'item' in my_list:  
    my_list.remove('item')  

конвертация input() без проверки:

# ОПАСНО:
age = int(input('Возраст: '))  # упадёт если введут не число  

# ПРАВИЛЬНО:
user_input = input('Возраст: ')  
if user_input.isdigit():  
    age = int(user_input)  

---

## 11. Мини-шпаргалка

базовый while → while условие:  
бесконечный цикл → while True:  
выход из цикла → break  
пропустить итерацию → continue  
флаг управления → active = True / active = False  
ввод от пользователя → input('подсказка: ')  
конвертировать ввод → int(user_input)  
проверить что цифры → user_input.isdigit()  
итерация списка → while my_list: + pop()  
удалить все вхождения → while 'x' in my_list: + remove('x')  
сбор в словарь → responses[name] = answer внутри while  