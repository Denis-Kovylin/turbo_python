'''Взять словарь с голосарием из предыдущего файла. Разширить еще 5ю понятиями о пайтоне.
Перебрать ключи-значения циклом и вывести принтом'''
gap ='\n'
glossary_dict = {}
glossary_dict['String'] = 'a sequence of characters enclosed in quotes, used to store and manipulate text data.'
glossary_dict['Integer'] = 'a whole number without a decimal point, can be positive, negative, or zero.'
glossary_dict['Float'] = 'a number with a decimal point, used for more precise numerical calculations.'
glossary_dict['List'] = 'an ordered and mutable collection of items enclosed in square brackets, can store mixed data types.'
glossary_dict['Dictionary'] = 'an unordered collection of key-value pairs enclosed in curly braces, each key must be unique.'
glossary_dict['Tuple'] = 'an ordered and immutable collection of items enclosed in parentheses, cannot be changed after creation.'
glossary_dict['Boolean'] = 'a data type with only two possible values: True or False, used in conditional expressions.'
glossary_dict['Function'] = 'a reusable block of code defined with the def keyword, that performs a specific task when called.'
glossary_dict['Loop'] = 'a control structure that repeatedly executes a block of code while a condition is true or for each item in a sequence.'
glossary_dict['Condition'] = 'an expression that evaluates to True or False, used with if/elif/else to control program flow.'

for key, value in glossary_dict.items():
    print(f'{gap}{key} - {value}')
print(gap*3)

'''Создать словарь на 3 итема. Ключ - река, значение - страна. Циклом вывести предложением 
используя и ключ и значение. Циклом вывести все реки-ключи. Циклом вывести все страны-значения'''
river_message = ' is the largest river in '
river_dict = {
    'ukraine': 'dnipro',
    'hina': 'yangtze',
    'usa': 'mississippi'
}

for cntr, riv in river_dict.items():
    if cntr == 'usa':
        print(f'{riv.title()}{river_message}{cntr.upper()}{gap}')
    else:
        print(f'{riv.title()}{river_message}{cntr.title()}{gap}')
print(gap*3)

for cntr in river_dict.keys():
    print(cntr)
print(gap)

for riv in river_dict.values():
    print(riv)
print(gap*3)

'''Опрос о языках прграмирования. Создать словарь: ключь-человек, значение-язык, на 3-5 айтемов. 
Создать список из людей. Те кто уже есть в словаре-опросе и несколько новых. Перебрать список циклом.
Для уже опрошенных - вывести благодарность, для неопрошеных вывести предложение прости опрос.'''
mess_thanks = ' thank you for taking the survey'
mess_invite = ' we invite you to take a survey'
list_of_respondents = ['jen', 'den', 'sarah', 'boris', 'edward', 'sasha', 'phil', 'max']
favorite_languages = {
    'jen': 'Pyphon',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for resp in list_of_respondents:
    if resp not in favorite_languages.keys():
        print(f'{resp.title()} - {mess_invite}{gap}')
    else:
        print(f'{resp.title()} - {mess_thanks}{gap}')



