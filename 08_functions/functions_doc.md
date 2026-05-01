# Python — Functions

---

## 1. Базовая структура функции

def имя_функции(параметры):  
    # тело функции  

def — ключевое слово объявления функции  
имя — snake_case  
вызов: имя_функции(аргументы)  

---

## 2. Функция без аргументов

def greet():  
    print('Hello!')  

greet() — вызов  

---

## 3. Позиционные аргументы

def make_shirt(size, text):  
    print(f'{size}: {text}')  

make_shirt('L', 'Just do it') — порядок важен, аргументы передаются по позиции  

---

## 4. Ключевые аргументы

make_shirt(text='Just do it', size='L') — порядок не важен, каждый аргумент привязан к имени  

---

## 5. Значения по умолчанию

def make_shirt(size='L', text='I love Python'):  
    print(f'{size}: {text}')  

make_shirt() — оба параметра дефолтные  
make_shirt('XL') — переопределён только size  
make_shirt(text='Go!') — переопределён только text  

параметры с дефолтом — всегда после параметров без дефолта  

---

## 6. Возврат значения

def city_country(city, country):  
    return f'{country.title()}, {city.title()}'  

result = city_country('kyiv', 'ukraine') — сохранить результат в переменную  
print(city_country('tokyo', 'japan')) — вывести результат напрямую  

функция без return возвращает None  

---

## 7. Возврат словаря

```python
def make_album(artist, album, qtt=None):
    music = {'artist': artist, 'album': album}
    if qtt:
        music['tracks'] = qtt
    return music
```

None как дефолт — стандартный способ сделать параметр необязательным  
if qtt: — срабатывает только если значение передано и не None  

---

## 8. *args — произвольное количество позиционных аргументов

```python
def make_sandwich(*toppings):
    for topping in toppings:
        print(topping)
```

make_sandwich('cheese') — один аргумент  
make_sandwich('cheese', 'ham', 'tomato') — три аргумента  

*args собирает все позиционные аргументы в кортеж  
имя args — условность, важна звёздочка *  

---

## 9. **kwargs — произвольные ключевые аргументы

```python
def build_profile(f_name, l_name, **kwargs):
    profile = {'first': f_name, 'last': l_name}
    for key, value in kwargs.items():
        profile[key] = value
    return profile
```

build_profile('jon', 'doe', city='dallas', age=30) — передать любое количество именованных аргументов  

**kwargs собирает все ключевые аргументы в словарь  
имя kwargs — условность, важны две звёздочки **  

---

## 10. Смешанные параметры — порядок объявления

def func(обязательный, дефолтный='x', *args, **kwargs):  

порядок строгий:  
1. позиционные (обязательные)  
2. позиционные с дефолтом  
3. *args  
4. **kwargs  

---

## 11. Передача списка в функцию

```python
def send_messages(mess_list, sent_list):
    while mess_list:
        msg = mess_list.pop()
        sent_list.append(msg)
```

send_messages(messages, sent) — передаётся ссылка, функция изменит оригинальный список  
send_messages(messages[:], sent) — передаётся копия среза, оригинал защищён  

---

## 12. Докстринга

```python
def make_car(brand, model, **props):
    '''Возвращает словарь с данными об автомобиле.'''
    ...
```

первая строка тела функции — строка-документация  
доступна через make_car.__doc__  
описывает ЧТО делает функция, не КАК  

---

## 13. Частые ошибки

параметр с дефолтом перед обязательным — SyntaxError:

```python
# НЕПРАВИЛЬНО:
def func(size='L', text):  # SyntaxError

# ПРАВИЛЬНО:
def func(text, size='L'):
```

изменение оригинального списка внутри функции:

```python
# ОПАСНО — оригинальный список опустеет:
def process(lst):
    while lst:
        item = lst.pop()

# ПРАВИЛЬНО — передавать копию:
process(my_list[:])
```

передача именованных аргументов в *args:

```python
# НЕПРАВИЛЬНО — cheese попадёт в **kwargs, а не *args:
def make_sandwich(*toppings, **extras):
    ...
make_sandwich(cheese='yes')

# ПРАВИЛЬНО:
make_sandwich('yes')
```

---

## 14. Мини-шпаргалка

объявить функцию → def name():  
вызвать функцию → name()  
позиционный аргумент → func(value)  
ключевой аргумент → func(param=value)  
дефолтное значение → def func(param='default'):  
необязательный параметр → def func(param=None):  
вернуть результат → return value  
произвольные позиционные → def func(*args):  
произвольные ключевые → def func(**kwargs):  
передать копию списка → func(my_list[:])  
докстринга → '''описание функции'''  
прочитать докстрингу → func.__doc__  
