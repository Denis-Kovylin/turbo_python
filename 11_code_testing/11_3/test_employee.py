import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.test_employee = Employee('Joe', 'Dou', 7000)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 12000)

    def test_give_custom_raise(self):
        self.test_employee.give_raise(10000)
        self.assertEqual(self.test_employee.salary, 17000)


if __name__ == '__main__':
    unittest.main()