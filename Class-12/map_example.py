# ------- list --------

num = [1, 2, 3, 4]

temp = map(lambda x: x ** 2, num)
print(list(temp))

# ------- string --------
s = "pYthOn"

res = list(map(lambda c: c.lower(), s) )

for i in res:
    print(i, end="")