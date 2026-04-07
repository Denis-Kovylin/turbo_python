'''Создать список юзером, один из которых admin. Перебрать список циклом FOR с конструкцией
if-elif-else. Воводить для юзеров стандартное приветствие, а для admin отличное от стандартного'''
gap = '\n'
users_list = ['Joe', 'Jack', 'Mary', 'Admin', 'Paul', 'Katy', 'Den']
empty_users_list = []

if not users_list:
    print('We need find some users')
else:
    for user in users_list:
        if user != 'Admin':
            print(f'Hello {user}, thank you for logging again:))')
        else:
            print(f'Hello {user}! Would you like to see a status report?')