def count_odd_even(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1

        else:
            odd += 1

    return [even, odd]

result = count_odd_even([1, 2, 3, 4, 5])
print(f"Total Even Number: {result[0]}")
print(f"Total Even Number: {result[1]}")