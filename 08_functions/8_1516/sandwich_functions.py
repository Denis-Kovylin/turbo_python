def make_sandwich(*toppings):
    '''Выводит описание сэндвича с переданными ингредиентами.'''
    print(f'\nWe made for you sandwich with:')
    for topping in toppings:
        print(f'\t{topping}')