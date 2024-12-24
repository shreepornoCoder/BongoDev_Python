numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# map
res = list(map(lambda x: x**2, numbers))
print("Squared Number List:", res)

# filter
res = list(filter(lambda x: x > 0, numbers))
print("Positive Number List:", res)

# sorted()
res = sorted(numbers, key=lambda x: abs(x))
print("Sorted in Ascending order by Absolute Value:", res) 

res = sorted(numbers, key=lambda x: abs(x), reverse=True)
print("Sorted in Descending order by Absolute Value:", res) 