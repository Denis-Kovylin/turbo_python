import unittest
from city_function import city_country


class TestCityFunction(unittest.TestCase):
    """Тесты для функции city_country."""

    def test_city_country(self):
        """Проверяет форматирование строки без указания населения."""
        location = city_country("japan", "tokio")
        self.assertEqual(location, "Japan, Tokio")

    def test_city_country_population(self):
        """Проверяет форматирование строки с указанием населения."""
        location_population = city_country("japan", "tokio", 55_000_000)
        self.assertEqual(location_population, "Japan, Tokio, Population - 55000000")


if __name__ == "__main__":
    unittest.main()

# NOTE Слудует помнить что ссаный юниттест запускается через терминал командой python3 file_name.py
