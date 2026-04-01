'''Создаем список концлагерей'''
gap = '\n'
camp_list = ['Dachau', 'Auschwitz', 'Ravensbrück', 'Buchenwald', 'Flossenbürg', 'Sachsenhausen', 'Mauthausen']
print(camp_list, gap)

'''Отсортируем его не изменяя. Выведем. Выведем оригинал, что  убедиться, что он не изминился'''
print(sorted(camp_list))
print(camp_list, gap)

'''Отобразим список в обратном порядке без его изменения. Убедимся в целостности оригинала'''
camp_list.reverse()
print(camp_list, gap)

'''Сортировка списка в обратном алфавитном порядке, без изменения оригенала'''
print(sorted(camp_list, reverse=True))
print(camp_list, gap)

'''Разворачиваем оригенальным список на "с конца" '''
camp_list.reverse()
print(camp_list, gap)

'''Сортируем оригенал по альфавиту'''
camp_list.sort()
print(camp_list, gap)

'''Сортируем оригенал в обратном алфавитном порядке'''
camp_list.sort(reverse=True)
print(camp_list)

