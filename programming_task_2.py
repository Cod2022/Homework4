n = 37
list1 = [i for i in range(1, n+1)]
list2 = []
list3 = []
for i in list1:
    if n % i == 0:
        list2.append(i)
    else:
        del list1 [1:-1]

list2 = [i for i in list2[1:]]

print(list2)
print(list1)
