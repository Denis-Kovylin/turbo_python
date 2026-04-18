'''Создать словарь. Ключи - имена людей, значения - списки любимых мест. Перебрать словарь циклом
и вывести: имя человека + все любимые места'''
gap = '\n'
space = '\t'
favorite_places = {
    'den': ['mountains', 'forest', 'beach'],
    'alex': ['museums', 'cafes', 'parks', 'galleries'],
    'kate': ['bookstores', 'gardens', 'seaside', 'old towns', 'vineyards'],
    'luke': []
}

if not favorite_places:
    print('dictionary is empty')
else:
    for person, places in favorite_places.items():
        if not places:
            print(f'{gap}{person.title()} favorite places list are empty')
        else:
            print(f'{gap}{person.title()} favorite places is:')
            for place in places:
                print(f'{space}{place.title()}')

'''Создать словарь. Ключи - имена людей, значения - списки любимых чисел. Перебрать циклом словарь
и вывести: имя -> все любимые числа'''
favorite_numbers = {
    'den': [7, 13, 42],
    'alex': [3, 33, 99, 100],
    'kate': [5, 15, 25, 35, 45],
    'max': [1, 8],
    'sara': [11, 22, 33],
    'jack': []
}

if not favorite_numbers:
    print('object totally empty')
else:
    for name, numbers in favorite_numbers.items():
        if not numbers:
            print(f'{gap}{name.title()} favorite numbers list is empty')
        else:
            print(f'{gap}{name.title()} favorite numbers: {numbers}')