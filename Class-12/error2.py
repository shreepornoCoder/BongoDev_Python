try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print(num1/num2) 

except Exception as e:
    if e == ZeroDivisionError:
        print("You can't divide by zero")  

    else:
        print("Enter Correct Input!")