'''Реализовать програму проверяющую есть ли желаемые для регистрации ники в списке ников уже зарегистрированых
юзеров. Нет - разрешать регистрацию; Есть - предлогать взять другой ник. Так же сравнивать ники в lower()'''
current_users = ['BoSS', 'Slayer', 'Nigma', 'HUNTER', 'baDBoy', 'NaRuTo']
new_users = ['Boss', 'Hitler', 'Johny', 'siGGGma', 'Hunter', 'kiLLer']

if not new_users:
    print('No new users to registration')
elif not current_users and len(new_users) > 0:
    for new_user in new_users:
        print(f'This nickname ({new_user}) is still available for registration.')
elif len(current_users) > 0 and len(new_users) > 0:
    current_lower = []
    new_lower = []
    for new_user in new_users:
        new_lower.append(new_user.lower())
    for current_user in current_users:
        current_lower.append(current_user.lower())
    for new in new_lower:
        if new in current_lower:
            print(f'This username ({new}) is not available for registration')
        else:
            print(f'This nickname ({new}) is still available for registration.')
else:
    print('Something went wrong. Please try again later.')

