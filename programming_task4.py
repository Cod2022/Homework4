import random

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
a = [2, 3, 4, 5]
print(get_polynominal(a))
