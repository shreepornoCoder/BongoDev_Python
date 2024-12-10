def myFunc(n):
    return lambda a: a*n

res = myFunc(5)
print(res(3))