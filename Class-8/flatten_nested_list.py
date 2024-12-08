def flatten_list(value):
    return [item for sublist in value for item in sublist]

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(flatten_list(nested_list))