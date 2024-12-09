def second_largest(numbers):
    main = list(set(numbers))
    main.sort(reverse=True)

    return main[1] if len(main) >= 2 else None

res = second_largest([1, 2])
print(f"Second Largest Element of the list is:", res)