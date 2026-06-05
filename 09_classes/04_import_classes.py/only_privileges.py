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
