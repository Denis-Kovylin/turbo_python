'''8-9. Сообщения
Передать список сообщений в функцию show_messages() — она просто выводит каждое.'''
# messages = ['hey what up', 'yo its a me mario', 'python is cool', 'send help']
# def show_messages(mess_list):
#     '''Выводит все сообщения из переданного списка.'''
#     for mess in mess_list:
#         print(mess)
# show_messages(messages)

'''8-10. Отправка сообщений
Функция send_messages() — выводит каждое сообщение, перемещает его из messages в sent_messages. 
После вызова вывести оба списка.'''
# messages = ['hey what up', 'yo its a me mario', 'python is cool', 'send help']
# sent_messages = []
# def send_messages(mess_list,snt_mess_list):
#     '''Выводит сообщения и перемещает их из очереди в список отправленных.'''
#     while mess_list:
#         current_mess = mess_list.pop()
#         print(f'Sending message: {current_mess}')
#         snt_mess_list.append(current_mess)
#     print('\nMessages')
#     print(mess_list)
#     print('\nSend messages: ')
#     for mess in snt_mess_list:
#         print(f'\t{mess}')
# send_messages(messages, sent_messages)

'''8-11. Заархивированные сообщения
То же что 8-10, но передаёшь функции копию списка messages[:]. 
После вызова оригинальный список должен остаться нетронутым.'''
# messages = ['hey what up', 'yo its a me mario', 'python is cool', 'send help']
# sent_messages = []
# def archive_messages(mess_list, origin_list, snt_list):
#     '''Отправляет копию сообщений, не изменяя оригинальный список.'''
#     while mess_list:
#         current_mess = mess_list.pop()
#         print(f'Sending message: {current_mess}')
#         snt_list.append(current_mess)
#     print('\nMessages:')
#     for mess in origin_list:
#         print(f'\t{mess}')
#     print('\nSent messages:')
#     for sent_mess in snt_list:
#         print(f'\t{sent_mess}')
# archive_messages(messages[:], messages, sent_messages)