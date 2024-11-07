num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
op = input("Enter the operator (+, -, *, /, %): ")

res = 0
if op == '+':
    res = num1 + num2
elif op == '-':
    res = num1 - num2
elif op == '*':
    res = num1 * num2
elif op == '/':
    res = num1 * num2
elif op == '%':
    res = num1 % num2
else:
    print("You have entered wrong operator!")

print(f"{num1} {op} {num2} = {res}")