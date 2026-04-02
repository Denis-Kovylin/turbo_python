'''Генерируем список от 1 до 1000000. Вывести все значения циклом FOR'''
gap = '\n'
num_list = list(range(1, 1000001))

for num in num_list:
    print(num)
print(gap*3)

'''Найдем найменшее и найбольшее число списка. Вычислим сумму его элементов'''
print(min(num_list), max(num_list), gap)
print(sum(num_list), gap*3)

'''Вывести все парные числа от 1 до 20 с помощью третьего аргумента range()'''
for num in range(2, 21, 2):
    print(num)
print(gap*3)

'''Создать и вывести числа от 3 до 30 которые кратные 3м'''
num_list = list(range(3, 32, 3))
for num in num_list:
    print(num)
print(gap*3)

'''Создать список ( генераторный ) "кубов" от 1 до 10. Вывести их циклом FOR'''
cube_list = [num**3 for num in range(1, 11)]
for item in cube_list:
    print(item)
print(gap*3)