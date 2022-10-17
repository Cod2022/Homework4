file = open('file.txt', 'r')

data = file.read()
numbers = []
for i in data:
    if i.isdigit():
        i = int(i)
        numbers.append(i)

print(numbers)
print(data)

exit()

strings = []
for i in digits:
    if i.isdigit():
        i = int(i)
        print(i)
    else:
        strings.append(i)
print(strings)
    


