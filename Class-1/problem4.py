import sys

num1 = input("Enter 1st Number: ")
num2 = input("Enter 2nd Number: ")

res = 0
flag = 0

if str(num1).isdigit() and str(num2).isdigit():
    num1 = int(num1)
    num2 = int(num2)
    op = input("Enter the operator (+, -, *, /, %): ")
    
    if op == '+':
        res = num1 + num2

    elif op == '-':
        res = num1 - num2

    elif op == '*':
        res = num1 * num2

    elif op == '/':
        res = num1 * num2

    elif op == '%':
        if num2 == 0:
            flag = -1
            print(f"{num1} cannot be divided by 0!")
            sys.exit(1)
        else:
            res = num1 % num2

    else:
        print("You have entered wrong operator!")

    if flag == 0:
        print(f"{num1} {op} {num2} = {res}")
        sys.exit(1)

else:
    print("Enter Valid Number!") 