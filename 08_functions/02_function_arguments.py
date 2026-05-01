'''8-3. Футболка
Написать функцию make_shirt() с двумя параметрами — размер и надпись.
Вызвать дважды: первый раз позиционными аргументами, второй раз ключевыми.'''
# def make_shirt(size, text):
#     '''Выводит описание футболки с указанным размером и надписью.'''
#     print(f'size: {size.title()}; slogan: {text.upper()}')
# make_shirt('l', 'just do it')
# make_shirt(text='Anima sana in corpore sano', size='xl')

'''8-4. Футболки L
Добавить дефолтные значения к параметрам — размер L и текст I love Python. 
Вызвать три раза: два с дефолтами (L и M), один с другим текстом.
'''
# def make_shirt(size='L', text='I love python'):
#     '''Выводит описание футболки; по умолчанию размер L с текстом I love Python.'''
#     print(f'size: {size}; text: {text}')
# make_shirt()
# make_shirt(size='XL')
# make_shirt(text='JS === shit')

'''8-5. Міста
Функция describe_city() — два параметра: город и страна. Страна имеет дефолтное значение. 
Вызвать три раза с разными городами.
'''
# def describe_city(city, country='USA'):
#     '''Выводит страну, в которой находится город; по умолчанию страна — USA.'''
#     print(f'{city.title()} is in {country}')
# describe_city('New York')
# describe_city('Dalas')
# describe_city('Tokio', 'Japan')

