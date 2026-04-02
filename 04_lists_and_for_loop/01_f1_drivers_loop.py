'''Создаем список пилотов Ф1 и служебные переменные'''
gap = '\n'
drivers_list = ['Max Verstappen', 'Lando Norris', 'George Russell', 'Charles Leclerc', 'Oscar Piastri', 'Fernando Alonso', 'Carlos Sainz']
message_top_driver = " - he's one of the best drivers of the 2025 Formula 1 season!"
message_love_f1 = "These drivers deserve to be in the running for the championship title. I'm thrilled about Formula 1)))"

'''С помощью цикла FOR выведем имя каждогно пилота'''
for driver in drivers_list:
    print(driver)
print(gap*3)

'''Выведем сообщение для каждого плоьа по очереди'''
for driver in drivers_list:
    print(f'{driver}{message_top_driver}{gap}')
print(gap*3)

'''Добавим еще одно сообщения в конце цикла'''
for driver in drivers_list:
    print(f'{driver}{message_top_driver}{gap}')
print(message_love_f1)

