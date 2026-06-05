import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""

    def setUp(self):
        """Создаёт тестового сотрудника перед каждым тестом."""
        self.test_employee = Employee("Joe", "Dou", 7000)

    def test_give_default_raise(self):
        """Проверяет повышение зарплаты на дефолтную сумму (5000)."""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 12000)

    def test_give_custom_raise(self):
        """Проверяет повышение зарплаты на произвольную сумму."""
        self.test_employee.give_raise(10000)
        self.assertEqual(self.test_employee.salary, 17000)


if __name__ == "__main__":
    unittest.main()
