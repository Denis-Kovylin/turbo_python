'''9-6. Визочок з морозивом
Класс IceCreamStand наследует Restaurant. Добавляешь атрибут flavors — список вкусов.
Метод show_flavors() выводит их. Создать экземпляр, вызвать метод.'''
class Restaurant:
    def __init__(self, name, cuisine):
        """Инициализирует ресторан с названием и типом кухни."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Выводит основную информацию о ресторане."""
        print('\nRestaurant info:')
        print(f'\tWe are called - {self.name}')
        print(f'\tWe cook the best {self.cuisine} dishes')

    def work_schedule(self):
        """Сообщает, что ресторан сейчас открыт."""
        print(f'\n{self.name} is open now!')

    def read_number_served(self):
        """Выводит текущее количество забронированных мест."""
        print(f'{self.number_served} - reserved seats')

    def set_number_served(self, setting_value):
        """Устанавливает новое количество забронированных мест."""
        self.number_served = setting_value
        print(f'\nYou have set the number of reserved seats - {self.number_served}')

    def increment_number_served(self, increment_value):
        """Увеличивает счётчик забронированных мест на заданное число."""
        self.number_served += increment_value
        print(f'\nYou have increased the number of reserved seats by {increment_value}')
        print(f'\nThe number of reserved seats - {self.number_served}')

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        """Инициализирует киоск мороженого, наследуя Restaurant, и задаёт список вкусов."""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'mint', 'pistachio']

    def show_flavors(self):
        """Выводит все доступные вкусы мороженого."""
        print(f'Flowers of icecream we have:')
        for flower in self.flavors:
            print(f'\t{flower}')

# stand_1 = IceCreamStand('SugarMommy', 'desserts')
# stand_1.show_flavors()

'''9-7. Адмін
Класс Admin наследует User. Атрибут privileges — список прав. Метод show_privileges() выводит их.
Создать экземпляр, вызвать метод.'''
class User:
    def __init__(self, f_name, s_name, age, country):
        """Инициализирует пользователя с именем, фамилией, возрастом и страной."""
        self.f_name = f_name
        self.s_name = s_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """Выводит полную информацию о пользователе."""
        print('\nUser info:')
        print(f'\tFirst name: {self.f_name}')
        print(f'\tSecond name: {self.s_name}')
        print(f'\tAge: {self.age} years old')
        print(f'\tCountry: {self.country}')

    def greet_user(self):
        """Выводит персональное приветствие пользователю."""
        print(f'Hello {self.f_name} {self.s_name} :))')

    def increment_login_attempts(self):
        """Увеличивает счётчик попыток входа на 1."""
        self.login_attempts += 1
        print(f'\nThe number of login attempts has increased. There are {self.login_attempts} attempts now.')

    def reset_login_attempts(self):
        """Сбрасывает счётчик попыток входа до нуля."""
        print(f'\nThe number of login attempts before the reset was {self.login_attempts}')
        self.login_attempts = 0
        print(f'The number of login attempts has been reset and is {self.login_attempts} now')

class Admin(User):
    def __init__(self, f_name, s_name, age, country):
        """Инициализирует администратора с правами доступа, наследуя User."""
        super().__init__(f_name, s_name, age, country)
        self.privileges = ['add post', 'delete post', 'ban user', 'edit post']

    def show_privileges(self):
        """Выводит список прав администратора."""
        print(f'\nAdmin as super user has permission to:')
        for privilege in self.privileges:
            print(f'\t{privilege}')

# amd_1 = Admin('John', 'Dou', 44, 'USA')
# amd_1.show_privileges()

'''9-8. Привілеї
Создать отдельный класс Privileges с атрибутом privileges и методом show_privileges().
Сделать экземпляр Privileges атрибутом класса Admin вместо простого списка.'''
class Privileges:
    def __init__(self):
        """Инициализирует объект с набором прав администратора по умолчанию."""
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can edit post']

    def  show_privileges(self):
        """Выводит список всех прав администратора."""
        print(f'\nAdmin as super user has permission to:')
        for privilege in self.privileges:
            print(f'\t{privilege}')

class Administrator(User):
    def __init__(self, f_name, s_name, age, country):
        """Инициализирует администратора с объектом прав Privileges, наследуя User."""
        super().__init__(f_name, s_name, age, country)
        self.privileges = Privileges()

# admstrt_1 = Administrator('Joana', 'Dou', 33, 'UAS')
# admstrt_1.privileges.show_privileges()

'''9-9. Оновити батарею
Берёшь пример electric_car.py из книги. Добавляешь в класс Battery метод upgrade_battery() —
если батарея меньше 100, ставит 100. Вызвать get_range() до и после.'''
class Car:
    def __init__(self, make, model, year):
        """Инициализирует автомобиль с маркой, моделью и годом выпуска."""
        self.make = make
        self.model = model
        self.year = year

class Battery:
    def __init__(self, battery_size=75):
        """Инициализирует батарею с заданной ёмкостью (по умолчанию 75 кВт·ч)."""
        self.battery_size = battery_size

    def get_range(self):
        """Выводит запас хода в зависимости от текущей ёмкости батареи."""
        if self.battery_size == 75:
            distance = 260
        elif self.battery_size == 100:
            distance = 315
        print(f'This vehicle can travel {distance} miles on its current battery charge ({self.battery_size}) kwt')

    def upgrade_battery(self):
        """Повышает ёмкость батареи до 100 кВт·ч, если она меньше этого значения."""
        if self.battery_size < 100:
            self.battery_size = 100
        print(f'The battery is fully charged and at {self.battery_size}% capacity')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Инициализирует электромобиль, наследуя Car, и добавляет батарею по умолчанию."""
        super().__init__(make, model, year)
        self.battery = Battery()

e_tron_1 = ElectricCar('audi', 'E-tron', 2018)
e_tron_1.battery.get_range()
e_tron_1.battery.upgrade_battery()
e_tron_1.battery.get_range()

