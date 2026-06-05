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
