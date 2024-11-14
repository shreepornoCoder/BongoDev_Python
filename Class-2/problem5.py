s = input("Enter a Sentence: ")

s = s.split()

res = {}

for char in s:
    res[char] = s.count(char)

print(res)