numbers = [2, 10, 4, 9, 7, 11, 8]
index = 0
max_num = 0
while index < len(numbers):
    if max_num < numbers[index]:
        max_num = numbers[index]
    
    index += 1

print(max_num)