def operateList(list1, list2):
    list3 = []
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            list3.append(list1[i])
    for j in range(len(list2)):
        if list2[j] % 2 != 0:
            list3.append(list2[j])
    return list3


list = operateList([1, 2, 45, 56], [34, 56, 1, 31])
print(list)
