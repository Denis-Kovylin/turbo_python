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
