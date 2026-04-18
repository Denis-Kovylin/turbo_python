# Python — Dictionaries

---

## 1. Создание словаря

my_dict = {'key': 'value'} — словарь с одним элементом  
empty_dict = {} — пустой словарь  

---

## 2. Добавление и изменение элементов

my_dict['new_key'] = 'new_value' — добавить или изменить элемент  

---

## 3. Обращение к значению

my_dict['key'] — по ключу (упадёт с KeyError если ключа нет)  
my_dict.get('key') — безопасно, вернёт None если ключа нет  
my_dict.get('key', 'default') — вернёт 'default' если ключа нет  

---

## 4. Удаление элементов

del my_dict['key'] — удалить элемент по ключу  

---

## 5. Перебор словаря циклом

for key, value in my_dict.items(): — перебор пар ключ-значение  
for key in my_dict.keys(): — перебор только ключей  
for value in my_dict.values(): — перебор только значений  

---

## 6. Проверка на пустоту

if not my_dict: — словарь пустой  
if my_dict: — словарь не пустой  

---

## 7. Проверка наличия ключа

if 'key' in my_dict: — ключ есть в словаре  
if 'key' not in my_dict: — ключа нет в словаре  

---

## 8. Вложенные структуры

словарь в словаре:

cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000
    }
}

доступ: cities['tokyo']['country']  

---

## 9. Список словарей

people = [
    {'name': 'den', 'age': 41},
    {'name': 'alex', 'age': 31}
]

перебор:

for person in people:
    print(person['name'])

---

## 10. Словарь со списками как значениями

favorite_places = {
    'den': ['mountains', 'forest', 'beach']
}

перебор:

for person, places in favorite_places.items():
    for place in places:
        print(place)

---

## 11. Числа с разделителем тысяч

population = 13_960_000 — читаемая запись больших чисел  
(подчёркивание игнорируется Python, только для читаемости)  

---

## 12. Частые ошибки

my_dict['key'] — упадёт если ключа нет, используй get()  
value.title() на числах — упадёт, title() только для строк  

---

## 13. Мини-шпаргалка

создать → {}  
добавить/изменить → dict['key'] = value  
получить → dict['key'] или dict.get('key')  
удалить → del dict['key']  
все пары → dict.items()  
все ключи → dict.keys()  
все значения → dict.values()  
проверить ключ → 'key' in dict  
пустой? → if not dict  
вложенный словарь → dict['key']['nested_key']  
список словарей → for item in list → item['key']  
словарь списков → for key, list in dict.items() → for item in list
