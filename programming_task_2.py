n = 35
list1 = [i for i in range(1, n+1)]
list2 = []
for i in list1:
    if n % i == 0:
        list2.append(i)
        list2 = list2[i+1:i-1]
    else:
        list3 = list2[i+1:i-1]
# list3 = [i for i in list1 if n % i == 0]
print(list2)
print(list3)