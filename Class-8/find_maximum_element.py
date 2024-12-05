def find_max(numbers):
    res = 0
    for i in numbers:
        if i > res:
            res = i
    
    return res

print(find_max([1, 7, 3, 4, 5]))