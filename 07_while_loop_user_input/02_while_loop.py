'''Спрашивать у пользователя ингридиенты для пиццы, пока он не введет "quit". Каждый раз, после
добавления ингридиента, выводить этот ингридиент ( в конце попробывать вывести все ингридиенты )'''
# pizza_quest = '\n( Enter "quit" when you are finished )'
# pizza_quest += '\nWhat would you like to add to your pizza?: '
# confirm_ingred = ' - has been added to your pizza'
# pizza_order = 'You ordered a pizza with: '
# pizza_toppings = []
#
# while True:
#     ingredient = input(pizza_quest)
#     if ingredient == 'quit':
#         break
#     print(f'\n{ingredient.title()}{confirm_ingred}')
#     pizza_toppings.append(ingredient)
#
# print(f'{pizza_order}')
# for topping in pizza_toppings:
#     print(f'\t{topping}')

'''Билеты в кино стоят: до 3х лет - бесплатно, от 3х до 12 - 10у.е, от - 15у.е.
Нужно спросить у юзера возраст, а потом вывести стоимость билета для него. "quit" - выход'''
# ticket_mess = 'A movie ticket for your age group costs - '
# age_quest = '\nPlease enter your age to see ticket prices: '
# user_age = input(age_quest)
# age = int(user_age)
# if age < 3:
#     print(f'{ticket_mess}free')
# elif age < 12:
#     print(f'{ticket_mess}10%')
# else:
#     print(f'{ticket_mess}15$')

'''На предыдущее задание прикрутить цикл While, break, continue, active, "quit" - выход'''
# ticket_mess = 'A movie ticket for your age group costs - '
# age_quest = '\nPlease enter your age to see ticket prices: '
# active = True
# while active:
#     user_age = input(age_quest)
#     if user_age == '':
#         print('This field is required')
#         continue
#     if user_age == 'quit':
#         print('bie-bie...X_x')
#         active = False
#         continue
#     if not user_age.isdigit():
#         print('digits only')
#         continue
#     else:
#         age = int(user_age)
#         if age < 3:
#             print(f'{ticket_mess}free')
#             break
#         elif age < 12:
#             print(f'{ticket_mess}10$')
#             break
#         elif age < 130:
#             print(f'{ticket_mess}15$')
#             break
#         else:
#             print('error')
#             continue



