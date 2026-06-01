# Python — Files & Exceptions

---

## 1. Чтение файла целиком

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
```

open() — открывает файл и возвращает объект файла  
with — автоматически закрывает файл после выхода из блока  
.read() — читает всё содержимое как одну строку  
.rstrip() — убрать лишний перенос строки в конце  

---

## 2. Построчное чтение

```python
with open('file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
```

перебор объекта файла в цикле — отдаёт по одной строке  
каждая строка содержит '\n' в конце — .rstrip() убирает его  

---

## 3. readlines() — список строк

```python
with open('file.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
```

.readlines() — читает все строки и возвращает список  
список доступен за пределами блока with  
удобно когда нужно работать со строками после закрытия файла  

---

## 4. Сборка строк файла в одну строку

```python
with open('file.txt') as file_object:
    lines = file_object.readlines()

content = ''
for line in lines:
    content += line.strip()
```

конкатенация с .strip() убирает пробелы и переносы с каждой строки  
результат — одна строка без пробельных символов между частями  

---

## 5. Кодировка файла

```python
with open('file.txt', encoding='utf-8') as file_object:
    content = file_object.read()
```

encoding='utf-8' — явно указать кодировку  
нужно если файл содержит символы вне ASCII или кодировка системы не совпадает  

---

## 6. Запись в файл — режим 'w'

```python
with open('output.txt', 'w') as file_object:
    file_object.write('Hello\n')
```

'w' — режим записи, создаёт файл или полностью перезаписывает существующий  
.write() не добавляет '\n' автоматически — нужно добавлять вручную  
если файла нет — Python создаст его  

---

## 7. Дозапись в файл — режим 'a'

```python
with open('guest_book.txt', 'a') as file_object:
    file_object.write(f'{user_name}\n')
```

'a' — режим дозаписи, не перезаписывает существующее содержимое  
используется когда нужно накапливать данные (логи, гостевые книги)  

---

## 8. try/except — базовая обработка исключений

```python
try:
    num = int(input('Enter a number: '))
except ValueError:
    print('Please enter a valid number!')
```

try — блок кода, который может вызвать исключение  
except ExceptionType — выполняется если возникло соответствующее исключение  
без обработки исключение прерывает программу с трейсбеком  

---

## 9. else — код при отсутствии исключения

```python
try:
    num_1 = int(input('First: '))
    num_2 = int(input('Second: '))
except ValueError:
    print('Invalid input!')
else:
    print(f'Sum: {num_1 + num_2}')
```

else — выполняется только если в try не было исключений  
хорошая практика — держать в try минимум кода, остальное выносить в else  

---

## 10. Частые исключения

ValueError — неверный тип данных при конвертации (int('abc'))  
ZeroDivisionError — деление на ноль (10 / 0)  
FileNotFoundError — файл не найден при открытии  

```python
try:
    with open('missing.txt') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found.')
else:
    print(content)
```

---

## 11. pass — тихое игнорирование исключения

```python
try:
    with open('file.txt') as f:
        content = f.read()
except FileNotFoundError:
    pass
```

pass — намеренно ничего не делать при исключении  
используется когда ошибка ожидаема и не критична  

---

## 12. json.dump() — сохранить данные в JSON

```python
import json

data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as f:
    json.dump(data, f)
```

json.dump(data, file) — сериализовать Python-объект в JSON и записать в файл  
подходит для словарей, списков, строк, чисел  

---

## 13. json.load() — загрузить данные из JSON

```python
import json

with open('data.json') as f:
    data = json.load(f)
```

json.load(file) — прочитать JSON из файла и вернуть Python-объект  
тип объекта соответствует содержимому JSON (dict, list, str, и т.д.)  

---

## 14. Паттерн: проверить — создать или загрузить

```python
import json

filename = 'username.json'

try:
    with open(filename) as f:
        name = json.load(f)
except FileNotFoundError:
    name = input('What is your name? ')
    with open(filename, 'w') as f:
        json.dump(name, f)
else:
    print(f'Welcome back, {name}!')
```

стандартный паттерн: сначала пробуем загрузить, при ошибке — запрашиваем и сохраняем  
позволяет «запоминать» данные между запусками программы  

---

## 15. Частые ошибки

запись без '\n' — весь текст склеится в одну строку:

```python
# НЕПРАВИЛЬНО:
file.write('line one')
file.write('line two')  # в файле: line oneline two

# ПРАВИЛЬНО:
file.write('line one\n')
file.write('line two\n')
```

режим 'w' уничтожает существующий файл:

```python
# ОПАСНО — каждый запуск стирает предыдущие данные:
with open('log.txt', 'w') as f:
    f.write(entry)

# ПРАВИЛЬНО для накопления:
with open('log.txt', 'a') as f:
    f.write(entry)
```

json.load() на несуществующем файле без обработки — программа упадёт:

```python
# НЕПРАВИЛЬНО:
with open('data.json') as f:   # FileNotFoundError если файла нет
    data = json.load(f)

# ПРАВИЛЬНО:
try:
    with open('data.json') as f:
        data = json.load(f)
except FileNotFoundError:
    data = None
```

---

## 16. Мини-шпаргалка

открыть файл → with open('file.txt') as f:  
прочитать целиком → f.read()  
прочитать построчно в список → f.readlines()  
итерация по строкам → for line in f:  
записать в файл (создать/перезаписать) → open('file.txt', 'w')  
дозаписать в файл → open('file.txt', 'a')  
записать строку → f.write('text\n')  
указать кодировку → open('file.txt', encoding='utf-8')  
перехватить исключение → try: / except ErrorType:  
код без ошибок → else:  
тихо проигнорировать → except ErrorType: pass  
сохранить в JSON → json.dump(data, f)  
загрузить из JSON → json.load(f)  
