s = input("Enter a string: ")

old_str = s.lower().strip()
new_str = old_str[::-1]

if new_str == old_str:
    print(True)

else:
    print(False)