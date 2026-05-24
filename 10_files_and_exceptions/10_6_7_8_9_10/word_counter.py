'''10-10. Поширені слова
Скачай любой текст с gutenberg.org, сохрани как .txt.
Читаешь файл, считаешь сколько раз встречается 'the' через .count(). Потом пробуешь 'the ' с пробелом.'''
mess_count = "The word 'the' appears "
mess_times = ' times in the file.'



try:
    with open('1984.txt', encoding='utf-8') as file_object:
        text = file_object.read()
except FileNotFoundError:
    print(f'File {file_object} doesn`t exist')
else:
    symbol_quantity = 0
    symbol_quantity += text.count('the')
    symbol_quantity += text.count(' the')
    symbol_quantity += text.count('The')
    print(mess_count, symbol_quantity, mess_times)