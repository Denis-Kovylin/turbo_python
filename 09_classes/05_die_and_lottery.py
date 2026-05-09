from random import randint, choice
'''9-13. Кубики
Класс Die с атрибутом sides=6. Метод roll_die() возвращает случайное число от 1 до sides.
Создать три кубика (6, 10, 20 сторон), каждый бросить 10 раз.'''
class Die:
    def __init__(self, sides=6):
        """Инициализирует кубик с заданным количеством сторон (по умолчанию 6)."""
        self.sides = sides

    def roll_the_dice(self):
        """Бросает кубик 10 раз и выводит результат каждого броска."""
        counter = 0
        while counter < 10:
            counter += 1
            print(f'\nAttempt: {counter}')
            result = randint(1, self.sides)
            print(f'\tResult: {result}')

# die_6 = Die()
# die_6.roll_the_dice()
# die_10 = Die(10)
# die_10.roll_the_dice()
# die_20 = Die(20)
# die_20.roll_the_dice()

'''9-14. Лотерея
Список/кортеж из 10 цифр и 5 букв. Случайно выбрать 4 элемента — это выигрышная комбинация.
Вывести сообщение.'''
def lottery():
    """Генерирует случайную выигрышную комбинацию из 4 элементов и выводит её."""
    lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    win_number = []
    while len(win_number) < 4:
        current_number = choice(lottery_pool)
        win_number.append(current_number)
    print(f'\nCongratulations! Ticket {win_number} has won a prize!')
# lottery()

'''9-15. Аналіз лотереї
Создать my_ticket из 4 элементов. Цикл крутится пока случайная выборка не совпадёт с твоим билетом.
Вывести сколько итераций понадобилось.'''
def analysis_lottery(ticket):
    """Считает, сколько случайных попыток нужно, чтобы совпасть с переданным билетом."""
    lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    analysis_attempt = 0
    win_number = []
    while win_number != ticket:
        win_number = []
        analysis_attempt += 1
        while len(win_number) < 4:
            current_number = choice(lottery_pool)
            win_number.append(current_number)
    print(f'It took {analysis_attempt} attempts to find matching numbers')

my_ticket = [3, 7, 'b', 'e']
analysis_lottery(my_ticket)