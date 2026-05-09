# Python — Classes

---

## 1. Базовая структура класса

```python
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
```

class — ключевое слово объявления класса  
имя класса — PascalCase (каждое слово с большой буквы)  
__init__ — специальный метод, вызывается автоматически при создании экземпляра  

---

## 2. self — ссылка на экземпляр

self.name = name — сохранить значение как атрибут конкретного экземпляра  
self — всегда первый параметр любого метода класса  
при вызове метода self передаётся автоматически — указывать его явно не нужно  

---

## 3. Методы экземпляра

```python
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f'{self.name} — {self.cuisine}')

    def work_schedule(self):
        print(f'{self.name} is open now!')
```

методы — это обычные функции внутри класса  
обращение к атрибутам внутри метода — через self  

---

## 4. Создание экземпляра и обращение к нему

res_1 = Restaurant('La Bella Italia', 'italian') — создать экземпляр  
res_1.name — обратиться к атрибуту  
res_1.describe() — вызвать метод  

---

## 5. Атрибуты с дефолтным значением

```python
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0  # не требует аргумента при создании
```

атрибут задаётся прямо в __init__ без параметра  
все экземпляры начнут с одинакового значения  

---

## 6. Изменение атрибутов

напрямую: res_1.number_served = 10  
через метод-сеттер:

```python
def set_number_served(self, value):
    self.number_served = value

def increment_number_served(self, amount):
    self.number_served += amount
```

методы предпочтительнее — позволяют добавить проверку значения  

---

## 7. Наследование

```python
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']
```

class Child(Parent) — объявить дочерний класс  
super().__init__() — вызвать __init__ родителя и получить его атрибуты  
после super() добавлять новые атрибуты дочернего класса  

дочерний класс автоматически наследует все методы родителя  

---

## 8. Переопределение метода родителя

```python
class ElectricCar(Car):
    def describe_battery(self):
        print('Electric vehicle')

    def work_schedule(self):  # метод есть в Car — переопределяем
        print('Available 24/7 for charging')
```

если метод с таким именем есть в дочернем классе — Python использует его  
метод родителя при этом игнорируется  

---

## 9. Композиция — класс как атрибут

```python
class Privileges:
    def __init__(self):
        self.privileges = ['add post', 'delete post', 'ban user']

    def show_privileges(self):
        for p in self.privileges:
            print(f'\t{p}')

class Administrator(User):
    def __init__(self, f_name, s_name, age, country):
        super().__init__(f_name, s_name, age, country)
        self.privileges = Privileges()  # экземпляр другого класса как атрибут
```

admstrt_1.privileges.show_privileges() — обращение через цепочку  
используется когда атрибуты и методы объекта разрастаются в отдельную сущность  

---

## 10. Импорт классов из модуля

from restaurant import Restaurant — импортировать один класс  
from user_module import User, Admin — импортировать несколько классов  
import restaurant — импортировать весь модуль (обращение: restaurant.Restaurant)  

```python
# main.py
from restaurant import Restaurant

bistro = Restaurant('Morning Flower', 'Breakfasts')
bistro.work_schedule()
```

каждый класс — в отдельном файле-модуле, если он используется в нескольких местах  

---

## 11. Докстринга класса и методов

```python
class Die:
    """Имитирует бросок кубика с заданным количеством сторон."""

    def __init__(self, sides=6):
        """Инициализирует кубик; по умолчанию 6 сторон."""
        self.sides = sides

    def roll_the_dice(self):
        """Бросает кубик 10 раз и выводит результат каждого броска."""
        ...
```

докстринга класса — сразу после class, перед __init__  
докстринга метода — первая строка тела метода  
доступна через Die.__doc__ и die_1.roll_the_dice.__doc__  

---

## 12. Частые ошибки

забыть self в параметрах метода — TypeError при вызове:

```python
# НЕПРАВИЛЬНО:
def describe(name):       # name получит экземпляр, а не строку
    print(name)

# ПРАВИЛЬНО:
def describe(self):
    print(self.name)
```

не вызвать super().__init__() в дочернем классе — атрибуты родителя не создадутся:

```python
# НЕПРАВИЛЬНО:
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        self.flavors = []  # self.name и self.cuisine недоступны

# ПРАВИЛЬНО:
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = []
```

обращение к атрибуту без self внутри метода — NameError:

```python
# НЕПРАВИЛЬНО:
def describe(self):
    print(name)       # NameError — name не существует в этой области

# ПРАВИЛЬНО:
def describe(self):
    print(self.name)
```

---

## 13. Мини-шпаргалка

объявить класс → class Name:  
конструктор → def __init__(self, ...):  
атрибут экземпляра → self.attr = value  
метод → def method(self):  
атрибут с дефолтом → self.counter = 0 в __init__  
создать экземпляр → obj = ClassName(args)  
обратиться к атрибуту → obj.attr  
вызвать метод → obj.method()  
наследование → class Child(Parent):  
инициализация родителя → super().__init__(args)  
композиция → self.component = OtherClass()  
импорт класса → from module import ClassName  
докстринга класса → """описание""" сразу после class  
