n = 36
list1 = [i for i in range(1, n+1)]
list2 = []
list3 = []
for i in list1:
    if n % i == 0:
        list2.append(i)

list2 = [i for i in list2[1:-1:]]



print(list2)
print(list1)