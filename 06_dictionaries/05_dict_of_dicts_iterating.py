'''Создать словарь. ключи - города, значения - словари -> ключи-значения - страна, население, интересный
факт про город. Перебрать словарь циклом и принтануть всю информацию про город'''
gap = '\n'
space = '\t'
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000,
        'fact': 'Tokyo is the most populous metropolitan area in the world'
    },
    'reykjavik': {
        'country': 'iceland',
        'population': 376_248,
        'fact': 'Reykjavik is the northernmost capital city in the world'
    },
    'montevideo': {
        'country': 'uruguay',
        'population': 1_380_000,
        'fact': 'Montevideo has the highest quality of life index in Latin America'
    }
}

if not cities:
    print('cities dictionary is empty')
else:
    for city, info in cities.items():
        if not info:
            print(f'{gap}no data about {city.title()}')
        else:
            print(f'{gap}{city.title()}')
            for key, value in info.items():
                if key == 'country':
                    print(f'{space}{key.title()}: {value.title()}')
                else:
                    print(f'{space}{key.title()}: {value}')

