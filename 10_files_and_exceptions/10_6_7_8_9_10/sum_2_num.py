'''10-6. Додавання
try/except — просишь два числа, складываешь, ловишь ValueError если ввели не число.'''
mess_first = 'Enter first number: '
mess_second = 'Enter second number: '
mess_error = 'Please enter valid numbers only!'
mess_result = 'Sum of your numbers is: '

num_1 = input(mess_first)
num_2 = input(mess_second)
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
except ValueError:
    print(mess_error)
else:
    result = num_1 + num_2
    print(f'{mess_result}{result}')