def count_odd_even(numbers):
    even = sum(1 for i in numbers if i % 2 == 0)
    odd = len(numbers) - even

    return [even, odd]

result = count_odd_even([1, 2, 3, 4, 5])
print(f"Total Even Number: {result[0]}")
print(f"Total Even Number: {result[1]}")