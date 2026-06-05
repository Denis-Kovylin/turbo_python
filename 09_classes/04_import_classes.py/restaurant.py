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
