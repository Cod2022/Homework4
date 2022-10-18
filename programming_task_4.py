import random
from random import randint

k = int(input('Введите коэффициент k: '))

def get_polynominal(list):
    list_len = len(list) - 1
    res_list = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            res_list = res_list + f'{list[i]}'
        elif list_len == 1:
            res_list = res_list + f'{list[i]}x + '
        else:
            res_list = res_list + f'{list[i]}x^{list_len} + '
        list_len = list_len - 1
    return res_list

def write_polynominal(n, file_name):
    numbers = [randint(1, 101) for _ in range(0, n+1)]
    result = get_polynominal(numbers)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(' '.join([str(i) for i in numbers]) + '\n')
        file.write(result)

write_polynominal(k, 'file.txt')
write_polynominal(k, 'file2.txt')

with open('file.txt', 'r') as file, open('file2.txt') as file2:
    print_file = [i for i in file.readlines()]
    print_file2 = [i for i in file2.readlines()]
    print(f'Коэффициэнты и многочлены 1-го файла: {print_file}')
    print(f'Коэффициенты и многочлены 2-го файла: {print_file2}')

