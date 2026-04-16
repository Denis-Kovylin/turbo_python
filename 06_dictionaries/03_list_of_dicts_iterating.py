'''Создать несколько словарей характерезиющих людей. Записать все словари в список. Пройти по списку
циклом и вывестю всю информацию про каждого человека'''
gap = '\n'
space = '\t'
den = {'first_name': 'denis', 'second_name': 'kovylin', 'age': 41, 'country': 'uruguay', 'city': 'montevideo'}
maxim = {'first_name': 'maxim', 'second_name': 'marshakov', 'age': 31, 'country': 'japan', 'city': 'tokio'}
asia = {'first_name': 'anastasia', 'second_name': 'khadeeva', 'age': 30, 'country': 'iceland', 'city': 'reykjavik'}
vlad = {}
people_list = [den, maxim, asia, vlad]

for person in people_list:
    if not person:
        print(f'This person are empty dictionary')
    else:
        for key, value in person.items():
            if key == 'first_name':
                print(f'First name: {value.title()}')
            if key == 'second_name':
                print(f'Second name: {value.title()}')
            if key == 'age':
                print(f'Age: {value}')
            if key == 'country':
                print(f'Country: {value.title()}')
            if key == 'city':
                print(f'City: {value.title()}')
        print(gap)
print(gap*3)

'''Создать несколько словарей с питамцами. В них должна храниться информация про питомца и хозяина.
Сохранить словари в список. Перебрать список циклом, так что б вывелась вся инфа из словарей'''
pet_1 = {'type': 'dog', 'breed': 'dachshund', 'name': 'mr pickles', 'owner': 'den'}
pet_2 = {'type': 'parrot', 'breed': 'budgerigar', 'name': 'phonia', 'owner': 'alex'}
pet_3 = {'type': 'cat', 'breed': 'maine coon', 'name': 'rhona', 'owner': 'kate'}
pet_4 = {}
pet_list = [pet_1, pet_2, pet_3, pet_4]

if not pet_list:
    print('This list is empty')
else:
    for pet in pet_list:
        if not pet:
            print('No data about this pet')
        else:
            for key, value in pet.items():
                print(f'{key.title()}: {value.title()}')
            print(gap)
