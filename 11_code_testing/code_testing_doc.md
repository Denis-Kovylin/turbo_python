# Python — Code Testing

---

## 1. Зачем тестировать код

unittest — встроенный модуль Python для автоматического тестирования  
тесты проверяют, что функции и классы работают ожидаемо при изменениях кода  
запуск тестов: python3 test_file.py в терминале  

---

## 2. Базовая структура теста

```python
import unittest
from my_module import my_function


class TestMyFunction(unittest.TestCase):

    def test_something(self):
        result = my_function(args)
        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
```

import unittest — подключить модуль тестирования  
класс теста — наследуется от unittest.TestCase  
каждый тест — метод, начинающийся с test_  
unittest.main() — запустить все тесты при прямом запуске файла  

---

## 3. assertEqual — основной метод проверки

```python
self.assertEqual(result, 'Japan, Tokyo')
```

assertEqual(a, b) — тест проходит, если a == b  
при несовпадении тест падает с подробным сообщением  

---

## 4. Частые методы проверки

assertEqual(a, b) — a равно b  
assertNotEqual(a, b) — a не равно b  
assertTrue(x) — x истинно  
assertFalse(x) — x ложно  
assertIn(item, list) — элемент присутствует в списке  
assertNotIn(item, list) — элемент отсутствует в списке  

---

## 5. Тестирование функции с опциональным параметром

```python
def city_country(country, city, population=""):
    """Возвращает строку формата 'Country, City' или 'Country, City, Population - N'."""
    if population:
        return f"{country}, {city}, population - {population}".title()
    return f"{country}, {city}".title()
```

```python
class TestCityFunction(unittest.TestCase):

    def test_city_country(self):
        location = city_country("japan", "tokio")
        self.assertEqual(location, "Japan, Tokio")

    def test_city_country_population(self):
        location = city_country("japan", "tokio", 55_000_000)
        self.assertEqual(location, "Japan, Tokio, Population - 55000000")
```

каждый тест — отдельный метод для одного сценария  
один тест — одна проверка, понятное имя описывает что тестируется  

---

## 6. setUp — общая подготовка перед каждым тестом

```python
class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.test_employee = Employee("Joe", "Dou", 7000)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 12000)

    def test_give_custom_raise(self):
        self.test_employee.give_raise(10000)
        self.assertEqual(self.test_employee.salary, 17000)
```

setUp() — вызывается автоматически перед каждым тест-методом  
self.attr в setUp — доступен во всех тестах класса  
исключает дублирование кода создания объектов  
каждый тест получает свежий экземпляр — тесты независимы друг от друга  

---

## 7. Тестирование класса

```python
class Employee:
    """Представляет сотрудника с именем, фамилией и зарплатой."""

    def __init__(self, f_name, s_name, salary):
        """Инициализирует сотрудника с именем, фамилией и начальной зарплатой."""
        self.f_name = f_name
        self.s_name = s_name
        self.salary = salary

    def give_raise(self, raising_value=5000):
        """Увеличивает зарплату на заданную сумму (по умолчанию 5000) и возвращает новое значение."""
        self.salary += raising_value
        return self.salary
```

тестировать нужно каждое поведение класса отдельно  
дефолтный аргумент и явный аргумент — разные тест-кейсы  

---

## 8. Именование тестов

имя тест-метода должно описывать что именно проверяется:  
test_city_country — базовый случай без населения  
test_city_country_population — расширенный случай с населением  
test_give_default_raise — повышение на дефолтную сумму  
test_give_custom_raise — повышение на произвольную сумму  

---

## 9. Структура тест-файла

```
project/
├── city_function.py      # тестируемый модуль
└── test_cities.py        # тесты к нему
```

тест-файл лежит рядом с тестируемым модулем  
имя тест-файла — test_ + имя модуля  
импорт тестируемой функции/класса в начале файла  

---

## 10. Результаты запуска тестов

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

. — один тест прошёл  
F — тест упал (AssertionError)  
E — тест вызвал исключение  
OK — все тесты прошли  

---

## 11. Частые ошибки

забыть унаследоваться от unittest.TestCase — тесты не запустятся:

```python
# НЕПРАВИЛЬНО:
class TestMyFunc:
    def test_something(self):
        ...

# ПРАВИЛЬНО:
class TestMyFunc(unittest.TestCase):
    def test_something(self):
        ...
```

имя тест-метода не начинается с test_ — метод будет проигнорирован:

```python
# НЕПРАВИЛЬНО:
def check_something(self):   # unittest не увидит этот метод
    ...

# ПРАВИЛЬНО:
def test_something(self):
    ...
```

изменять self.attr в setUp внутри теста — следующий тест получит грязное состояние:

```python
# setUp создаёт свежий объект перед каждым тестом автоматически
# не нужно сбрасывать состояние вручную
```

---

## 12. Мини-шпаргалка

подключить модуль → import unittest  
базовый класс → class TestName(unittest.TestCase):  
подготовка данных → def setUp(self):  
тест-метод → def test_имя(self):  
проверить равенство → self.assertEqual(a, b)  
проверить неравенство → self.assertNotEqual(a, b)  
проверить истинность → self.assertTrue(x)  
проверить наличие → self.assertIn(item, list)  
запустить тесты → python3 test_file.py  
