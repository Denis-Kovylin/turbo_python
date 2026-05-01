'''8-12. Бутерброд
Функция принимает произвольное количество аргументов (*args) — ингредиенты. Выводит описание сэндвича.
Вызвать 3 раза с разным количеством ингредиентов.'''
def make_sandwich(*toppings):
    print(f'\nWe made for you sandwich with:')
    for topping in toppings:
        print(f'\t{topping}')
make_sandwich('ewfwe', 'dewdwdw', 'dewdwdw')
make_sandwich('efwefwefwe', 'wdwedwdw')
make_sandwich('cece', 'dewdewwed', 99, 'dewdewdew')

'''8-13. Профиль пользователя
Функция build_profile() принимает имя, фамилию и произвольные ключевые аргументы (**kwargs). 
Возвращает словарь. Вызвать со своими данными + 3 доп. характеристики.'''
def build_profile(f_name, l_name, **propertys):
    user_dict = {}
    user_dict['first_name'] = f_name
    user_dict['second_name'] = l_name
    for key, value in propertys.items():
        user_dict[key] = value
    return user_dict
print(f'\n{build_profile('jon', 'dou', country='usa', city='dallas')}')


'''8-14. Автомобили
Функция make_car() принимает марку, модель и произвольные ключевые аргументы. Возвращает словарь.'''
def make_car(brand, model, **propertys):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in propertys.items():
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(f'\n{car}')