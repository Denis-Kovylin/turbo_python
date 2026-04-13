'''Создать словарь человека. Записать туда информацию ключами-значениями. Имя, фамилия, возраст,
 страна, город'''
gap = '\n'
human_dict = {}
human_dict['first_name'] = 'John'
human_dict['second_name'] = 'Dou'
human_dict['age'] = 21
human_dict['country'] = 'USA'
human_dict['city'] = 'New York'
print(f'key - first_name: value - {human_dict['first_name']}')
print(f'key - second_name: value - {human_dict['second_name']}')
print(f'key - age: value - {human_dict['age']}')
print(f'key - country: value - {human_dict['country']}')
print(f'key - city: value - {human_dict['city']}{gap*3}')

'''Создать список "любимых чисел" и людей. Присвоить людям ( ключам ) любимый числа ( значения ).
Вывести на экран имена людей и числа'''
favorite_number = {}
favorite_number['Max'] = 27
favorite_number['Den'] = 38
favorite_number['John'] = 88
favorite_number['Joe'] = 1
favorite_number['Bob'] = 33
print(f'Max favorite number is: {favorite_number['Max']}')
print(f'Den favorite number is: {favorite_number['Den']}')
print(f'John favorite number is: {favorite_number['John']}')
print(f'Joe favorite number is: {favorite_number['Joe']}')
print(f'Bob favorite number is: {favorite_number['Bob']}{gap*3}')

'''Создать голосарий с определениями из пайтона. При выводе для практики будем использовать get()'''
glossary_dict = {}
glossary_dict['String'] = 'a sequence of characters enclosed in quotes, used to store and manipulate text data.'
glossary_dict['Integer'] = 'a whole number without a decimal point, can be positive, negative, or zero.'
glossary_dict['Float'] = 'a number with a decimal point, used for more precise numerical calculations.'
glossary_dict['List'] = 'an ordered and mutable collection of items enclosed in square brackets, can store mixed data types.'
glossary_dict['Dictionary'] = 'an unordered collection of key-value pairs enclosed in curly braces, each key must be unique.'
print(f'String - {glossary_dict.get('String', 'Key with this name not found!')}')
print(f'Integer - {glossary_dict.get('Integer', 'Key with this name not found!')}')
print(f'Float - {glossary_dict.get('Float', 'Key with this name not found!')}')
print(f'List - {glossary_dict.get('List', 'Key with this name not found!')}')
print(f'Dictionary - {glossary_dict.get('Dictionary', 'Key with this name not found!')}')
print(f'Boolean - {glossary_dict.get('Boolean', 'Key with this name not found!')}')