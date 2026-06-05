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


class Admin(User):
    def __init__(self, f_name, s_name, age, country):
        """Инициализирует администратора с правами доступа, наследуя User."""
        super().__init__(f_name, s_name, age, country)
        self.privileges = ["add post", "delete post", "ban user", "edit post"]

    def show_privileges(self):
        """Выводит список прав администратора."""
        print(f"\nAdmin as super user has permission to:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Privileges:
    def __init__(self):
        """Инициализирует объект с набором прав администратора по умолчанию."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can edit post",
        ]

    def show_privileges(self):
        """Выводит список всех прав администратора."""
        print(f"\nAdmin as super user has permission to:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Administrator(User):
    def __init__(self, f_name, s_name, age, country):
        """Инициализирует администратора с объектом прав Privileges, наследуя User."""
        super().__init__(f_name, s_name, age, country)
        self.privileges = Privileges()
