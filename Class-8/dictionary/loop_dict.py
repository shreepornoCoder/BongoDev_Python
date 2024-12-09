from icecream import ic

student = {"name":"Shreeporno", "roll":55, "grade":9}

# For Only Getting The Keys of the dictionary
for key in student:
    print(key)

print("\n")

# For Only Getting The values of the dictionary
for val in student.values():
    print(val)

print("\n")

for keys, val in student.items():
    print(keys, ":", val)

print("\n")
for keys, val in enumerate(student):
    print(keys, ":", val)