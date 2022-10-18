with open('file.txt', 'r') as file, open('file2.txt', 'r') as file2:
    data = file.read()
    data2 = file2.read()
    numbers = []
    numbers2 = []
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers.append(i)
    # for i in data2:
    #     if i.isdigit():
    #         i = int(i)
    #         numbers2.append(i)

print(numbers)
print(numbers2)
print(data)

# exit()

# strings = []
# for i in digits:
#     if i.isdigit():
#         i = int(i)
#         print(i)
#     else:
#         strings.append(i)
# print(strings)
    

# with open('file.txt') as file:
#     num = [int(i) for i in file.readline().split()]

# print(num)