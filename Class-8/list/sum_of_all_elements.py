def sum_of_element(numbers:list):
    total = 0
    for num in numbers:
        total += num

    return total

result = sum_of_element([1, 2, 3, 4, 5])
print(result)

print(sum([1, 2, 3, 4, 5]))