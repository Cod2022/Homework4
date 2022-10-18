
from programming_task_4 import get_polynominal

with open('file.txt') as file, open('file2.txt') as file2:
    file1_data = [int(i) for i in file.readline().split()]
    file2_data = [int(i) for i in file2.readline().split()]
if len(file2_data) == len(file1_data):
    res_list = [a + b for a, b in zip(file1_data, file2_data)]


with open('file3.txt', 'w') as file3:
    file3.write(get_polynominal(res_list))
    
with open('file3.txt', 'r') as print_file3:
    print_file = [i for i in print_file3.readlines()]
    print(f'Сумма коэффициентов 1-го и 2-го файлов: {print_file}')


