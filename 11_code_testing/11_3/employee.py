class Employee:

    def __init__(self, f_name, s_name, salary):
        self.f_name = f_name
        self.s_name = s_name
        self.salary = salary

    def give_raise(self, raising_value=5000):
        self.salary += raising_value
        return self.salary