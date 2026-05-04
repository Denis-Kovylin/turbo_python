'''9-1. Ресторан
Создать класс Restaurant с двумя атрибутами — название и тип кухни. Два метода — описать ресторан
и сообщить что он открыт. Создать один экземпляр, вывести атрибуты и вызвать оба метода.'''
# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#
#     def describe(self):
#         print('\nRestaurant info:')
#         print(f'\tWe are called - {self.name}')
#         print(f'\tWe cook the best {self.cuisine} dishes')
#
#     def work_schedule(self):
#         print(f'\n{self.name} is open now!')
#
# res_1 =Restaurant('La Bella Italia', 'italian')
# print(res_1.name)
# print(res_1.cuisine)
# res_1.describe()
# res_1.work_schedule()

'''9-2. Три ресторана
Берёшь класс из 9-1. Создаёшь три разных экземпляра и вызываешь describe_restaurant() для каждого.'''
# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#
#     def describe(self):
#         print(f'\nRestaurant info:')
#         print(f'Name - {self.name}')
#         print(f'Cuisine - {self.cuisine}')
#
# res_1 = Restaurant('Sushi Taro', 'japanese')
# res_2 = Restaurant('El Rancho', 'mexican')
# res_3 = Restaurant('The Pig & Bull', 'british')
#
# res_1.describe()
# res_2.describe()
# res_3.describe()

'''9-3. Пользователи
Класс User — атрибуты: имя, фамилия, возраст, страна. Метод describe_user() выводит всю инфу. 
Метод greet_user() — персональное приветствие. Создать несколько экземпляров, вызвать оба метода.'''
# class User:
#     def __init__(self, f_name, s_name, age, country):
#         self.f_name = f_name
#         self.s_name = s_name
#         self.age = age
#         self.country = country
#
#     def describe_user(self):
#         print('\nUser info:')
#         print(f'\tFirst name: {self.f_name}')
#         print(f'\tSecond name: {self.s_name}')
#         print(f'\tAge: {self.age} years old')
#         print(f'\tCountry: {self.country}')
#
#     def greet_user(self):
#         print(f'Hello {self.f_name} {self.s_name} :))')
#
# u1 = User('Denis', 'Kovylin', 41, 'Uruguay')
# u2 = User('Alex', 'Smith', 28, 'USA')
# u3 = User('Kate', 'Brown', 33, 'Iceland')
#
# u1.greet_user()
# u1.describe_user()
# print('\n')
# u2.greet_user()
# u2.describe_user()
# print('\n')
# u3.greet_user()
# u3.describe_user()
