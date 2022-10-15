number = int(input('Введите число: '))

def prime_factors_list(number):
    list1 = list()
    div = 2
    while div <= number:
        if number % div == 0:
            list1.append(div)
            number = number / div
        else:
            div +=1
    return list1

print(f'Простые делители для числа {number}: {prime_factors_list(number)}')