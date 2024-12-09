def reverse_list(my_list):
    result = []
    for i in range(len(my_list)-1, -1, -1):
        result.append(my_list[i])

    return result

print(reverse_list([1, 2, 6, 4, 5]))
