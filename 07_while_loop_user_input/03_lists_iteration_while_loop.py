'''7-8. Кафе
Два списка — заказы и готовые. Цикл забирает сэндвич из заказов, "готовит" и перекладывает в готовые.
В конце выводит все готовые.'''
# sandwich_orders = ['club', 'pastrami', 'blt', 'veggie', 'pastrami', 'reuben', 'pastrami']
# finished_sandwiches = []
# mess_making = 'I made your '
# mess_done = '\nAll sandwiches are ready! Here is the list:'
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f'{mess_making}{current_sandwich} sandwich :)\n')
#     finished_sandwiches.append(current_sandwich)
# print('\tCooking done!\n')
# print(f'{mess_done}')
# for sandwich in finished_sandwiches:
#     print(f'{sandwich}')

'''7-9. Жодної пастроми
Берёшь список из 7-8 (там pastrami встречается 3 раза — специально). 
В начале выводишь сообщение что пастрома закончилась. 
Потом циклом while удаляешь все pastrami из заказов. Убеждаешься что в готовых тоже нет.'''
# mess_no_pastrami = 'Sorry, we are out of pastrami today!'
# sandwich_orders = ['club', 'pastrami', 'blt', 'veggie', 'pastrami', 'reuben', 'pastrami']
# finished_sandwiches = []
# mess_making = 'I made your '
# mess_done = '\nAll sandwiches are ready! Here is the list:'
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     if current_sandwich == 'pastrami':
#         continue
#     else:
#         print(f'{mess_making}{current_sandwich} sandwich')
#         finished_sandwiches.append(current_sandwich)
# print(f'{mess_done}')
# for sandwich in finished_sandwiches:
#     print(f'\t{sandwich}')

'''7-10. Идеальный отпуск
Опрос в цикле — спрашиваешь имя и место мечты, записываешь в словарь. quit — выход. 
В конце выводишь все ответы.'''
# responses = {}
# mess_invite = 'If you could visit one place in the world, where would you go?: '
# mess_name = 'What is your name?: '
# mess_results = '\n--- Poll Results ---'
# switcher = True
# while switcher:
#     user_name = input(mess_name)
#     user_spot = input(mess_invite)
#     responses[user_name] = user_spot
#     next_respondent = input('Your friend wants to take the survey too? (y|n): ')
#     if next_respondent == 'y':
#         continue
#     else:
#         switcher = False
#         print(mess_results)
#         for name, spot in responses.items():
#             print(f'\t{name.title()}: {spot.title()}')
