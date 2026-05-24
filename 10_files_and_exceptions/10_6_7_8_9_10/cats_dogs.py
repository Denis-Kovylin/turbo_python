'''10-8. Коти та собаки
Создай два файла cats.txt и dogs.txt с именами животных.
Читаешь оба файла, ловишь FileNotFoundError если файл не найден.'''
fn_dogs = 'dogs.txt'
fn_cats = 'cats.txt'

try:
    with open(fn_cats, encoding='utf-8') as file:
        content_dog = file.read()
except FileNotFoundError:
    print('Sorry, the file was not found.')
else:
    print(content_dog)

try:
    with open(fn_dogs, encoding='utf-8') as file:
        content_cat = file.read()
except FileNotFoundError:
    print('Sorry, the file was not found.')
else:
    print(content_cat)
