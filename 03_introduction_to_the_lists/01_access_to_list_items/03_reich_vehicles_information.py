# Создан список транспортных средств.
# По будет выводиться описание каждого из них с обращением к их списку по индексу

gap = '\n'
vehicles_list = ['Horch', 'Mercedes-Benzes', 'BMW', 'Opel', 'Zundapp']

print(f'{gap}{vehicles_list[0]} manufactured tractors in the late 19th century. '
      f'In the early 20th century, the company shifted its focus to premium roadsters, '
      f'which Adolf Hitler was so fond of.{gap}')
print(f'At the same time, the Reich’s top leadership preferred vehicles of the {vehicles_list[1]}{gap}')
print(f'{vehicles_list[2]}s were widely used by Reich officers. They were not much less comfortable than {vehicles_list[1]}.{gap}')
print(f'Ordinary Wehrmacht soldiers were content with {vehicles_list[3]} vehicles, which produced SUVs and trucks.{gap}')
print(f'The powerful and reliable {vehicles_list[4]} firmly established itself in the military motorcycle market, displacing {vehicles_list[2]}.')
