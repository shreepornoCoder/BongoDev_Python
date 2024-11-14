s1 = input("Enter a word: ")
s2 = s1

# way-1
s1 = list(set(list(s1.strip())))
print(''.join(s1))

# way-2
res = []
for char in s2:
    if char not in res:
        res.append(char)

print(''.join(res))