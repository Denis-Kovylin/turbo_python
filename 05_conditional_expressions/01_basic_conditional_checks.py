"""В этом файле будут базовые проверки непонятного мне характера. Сделаные по примеру из книги"""

gap = "\n"
car = "subaru"
print(car)
print(f"Is car == subaru? I predict True")
print(f'{car == "subaru"}')
print(f"Is car == audi? I predict False")
print(f'{car == "audi"}{gap}')

color = "red"
print(color)
print(f"Is color == red? I predict True")
print(f'{color == "red"}')
print(f"Is color == yellow? I predict False")
print(f'{color == "yellow"}{gap}')

country = "China"
print(country)
print(f"Is country == China? I predict True")
print(f'{country == "China"}')
print(f"Is country == Korea? I predict False")
print(f'{country == "Korea"}{gap}')

consol = "xbox"
print(consol)
print("Is consol == xbox? I predict True")
print(f'{consol == "xbox"}')
print("Is consol == play station? I predict False")
print(f'{consol == "play station"}{gap}')

music = "rock"
print(music)
print("Is music == rock? I predict True")
print(f'{music == "rock"}')
print("Is music == rap? I predict False")
print(f'{music == "rap"}{gap*3}')

"""Создать больше проверок: Для типа string; с lower(); для numdurs с <,>, ==, <=, >=; 
С использованием or, and; На наличие элемента в списке; На отсутствие элемента в списке"""
sting = "qwerty"
print(f"The string == {sting}")
print(f"qwerty - {sting == 'qwerty'}")
print(f'ytrewq - {sting == "ytrewq"}{gap}')

name = "John Dou"
print(f"name == {name}")
print(f"{name.lower()} - {name.lower() == name.lower()}")
print(f"{name} - {name == name.lower()}{gap}")

number = 1488
print(f"number == {number}")
print(f"=={number} - {number == number}")
print(f"==1500 - {number == 1500}")
print(f">100 - {number > 100}")
print(f">1500 - {number > 1500}")
print(f"<1500 - {number < 1500}")
print(f"<1000 - {number < 1000}")
print(f">=1487 - {number >= 1487}")
print(f">=1489 - {number >= 1489}")
print(f"<=1490 - {number <= 1490}")
print(f"<=1450 - {number <= 1450}{gap}")

number = 1488
print(f"number == {number}")
print(f">1000 or <2000 - {number > 1000 or number < 2000}")
print(f">10000 or ==1489 - {number > 10000 or number == 1489} ")
print(f">1000 and <2000 - {number > 1000 and number < 2000}")
print(f"==1488 and > 1500 - {number == 1488 and number > 1500}{gap}")

my_list = [num for num in range(0, 10)]
print(my_list)
print(f"8 in list - {8 in my_list}")
print(f"10 in list - {10 in my_list}")
print(f"11 not in list - {11 not in my_list}")
print(f"7 not in list - {7 not in my_list}")
