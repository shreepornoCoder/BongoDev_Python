from icecream import ic

def getting_duplicate(numbers:list):
    num = []
    
    for i in range(0, len(numbers)-1):
        for j in range(i, len(numbers)):
            if i != j:
                if numbers[i] == numbers[j]:
                    num.append(numbers[i])

    return num


a = [1, 2, 2, 4, 4, 3, 5, 5]
new_list = []
for val in a:
    if val not in new_list:
        new_list.append(val)

res = getting_duplicate(a)
print("Duplicate Values: ", res)
print("After Removing Duplicate Values: ", new_list)