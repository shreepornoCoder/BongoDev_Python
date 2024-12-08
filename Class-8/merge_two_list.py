def merger(list1, list2):
    list1 = list(set(list1))
    list2 = list(set(list2))

    new_list = []

    for i in range(0, max(len(list1), len(list2))):
        if i < len(list1):
            new_list.append(list1[i])

        if i < len(list2):
            new_list.append(list2[i])

    return list(set(new_list))

res = merger([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
print(res)