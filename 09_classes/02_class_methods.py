"""9-4. Количество клиентов
Берёшь класс Restaurant из 9-1. Добавляешь атрибут number_served = 0 прямо в __init__. Потом три метода:
вывести текущее значение
set_number_served() — установить новое значение
increment_number_served() — добавить к текущему значению"""


class Restaurant:
    def __init__(self, name, cuisine):
        """Инициализирует ресторан с названием и типом кухни."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Выводит основную информацию о ресторане."""
        print("\nRestaurant info:")
        print(f"\tWe are called - {self.name}")
        print(f"\tWe cook the best {self.cuisine} dishes")

    def work_schedule(self):
        """Сообщает, что ресторан сейчас открыт."""
        print(f"\n{self.name} is open now!")

    def read_number_served(self):
        """Выводит текущее количество забронированных мест."""
        print(f"{self.number_served} - reserved seats")

    def set_number_served(self, setting_value):
        """Устанавливает новое количество забронированных мест."""
        self.number_served = setting_value
        print(f"\nYou have set the number of reserved seats - {self.number_served}")

    def increment_number_served(self, increment_value):
        """Увеличивает счётчик забронированных мест на заданное число."""
        self.number_served += increment_value
        print(f"\nYou have increased the number of reserved seats by {increment_value}")
        print(f"\nThe number of reserved seats - {self.number_served}")


# rest_1 = Restaurant('La Bella Italia', 'italian')
# rest_1.read_number_served()
# rest_1.set_number_served(5)
# rest_1.increment_number_served(2)

"""9-5. Попытки авторизации
Берёшь класс User из 9-3. Добавляешь атрибут login_attempts = 0. Два новых метода:
increment_login_attempts() — добавляет 1 к счётчику
reset_login_attempts() — сбрасывает в 0
Создать экземпляр, вызвать инкремент несколько раз, вывести значение, сбросить, вывести снова."""


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
        print("\nUser info:")
        print(f"\tFirst name: {self.f_name}")
        print(f"\tSecond name: {self.s_name}")
        print(f"\tAge: {self.age} years old")
        print(f"\tCountry: {self.country}")

    def greet_user(self):
        """Выводит персональное приветствие пользователю."""
        print(f"Hello {self.f_name} {self.s_name} :))")

    def increment_login_attempts(self):
        """Увеличивает счётчик попыток входа на 1."""
        self.login_attempts += 1
        print(
            f"\nThe number of login attempts has increased. There are {self.login_attempts} attempts now."
        )

    def reset_login_attempts(self):
        """Сбрасывает счётчик попыток входа до нуля."""
        print(
            f"\nThe number of login attempts before the reset was {self.login_attempts}"
        )
        self.login_attempts = 0
        print(
            f"The number of login attempts has been reset and is {self.login_attempts} now"
        )


# user_1 = User('Denis', 'Kovylin', 41, 'Uruguay')
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print(user_1.login_attempts)
# user_1.reset_login_attempts()
# print(user_1.login_attempts)
