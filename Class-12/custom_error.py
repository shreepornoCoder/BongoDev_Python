x = 7

try:
    if x % 2 == 0:
        raise Exception("I will only print if x is even!")
    else:
        print(x)

except Exception as e:
    print(e)
