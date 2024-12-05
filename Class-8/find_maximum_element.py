from icecream import ic

def find_max(numbers):
    res = 0
    for i in numbers:
        if i > res:
            res = i
    
    return res

ic(find_max([1, 7, 3, 4, 5]))