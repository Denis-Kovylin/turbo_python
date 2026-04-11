'''Создать список порядковых числительных. Пройтись по ним циклом с if-elif-else. Вывести каждое
принтом с провилным окончанием ( 1st, 2nd, 3rd, 4-5-6....th'''
num_list = [num for num in range(1, 10)]
gap = '\n'

if not num_list:
    print('list is empty')
else:
    for num in num_list:
        if num == 1:
            print(f'{num}st{gap}')
        elif num == 2:
            print(f'{num}nd{gap}')
        elif num == 3:
            print(f'{num}rd{gap}')
        elif num >= 4 and num <= 9:
            print(f'{num}th{gap}')
        else:
            print('This value is not processed')




