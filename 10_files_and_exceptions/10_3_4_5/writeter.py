'''10-3. Гість
Просто input() для имени, и записать в файл guest.txt через open() в режиме 'w'.'''
# user_name = input('What is your name?: ')
# if not user_name:
#     print('Error. Something went wrong')
# else:
#     with open('guest.txt', 'w') as guest:
#         guest.write(user_name)
#     print(f'Thank you for visiting, {user_name}!')

'''10-4. Гостьова книга
Цикл while, спрашивает имя пока не введут quit. Каждое имя записать в guest_book.txt. 
Открывать файл в режиме 'a' (append) чтобы не перезаписывать.'''
# while True:
#     user_name = input('What is your name? (or quit for exit): ')
#     if user_name == 'quit':
#         break
#     else:
#         with open('guest_book.txt', 'a') as file_object:
#             file_object.write(f'{user_name}\n')
#         print(f'Hello {user_name}')
#         print(f'{user_name} has been logged in guest book')
#         continue

'''10-5. Опитування про програмування
То же что 10-4 но спрашиваешь почему нравится программирование. Записываешь причины в файл.'''
# while True:
#     reason = input('Why do you like programming? (or "quit" to exit): ')
#     if reason == 'quit':
#         break
#     else:
#         with open('programming_survey.txt', 'a') as file_object:
#             file_object.write(f'{reason}\n')
#         print('Thanks for your answer!')
