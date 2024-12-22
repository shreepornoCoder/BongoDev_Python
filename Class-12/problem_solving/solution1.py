def division(x, y):
    return x / y    

run = True
while run:
    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))

        if num2 == 0:
            raise ZeroDivisionError

    except ZeroDivisionError:
        print("Division by zero is not allowed")
    
    except ValueError:
        print("Please enter a valid number")
    
    except:
        print("An error occurred")

    else:
        run = False
        
# ----------------------------
result = division(num1, num2)

print("{}/{} = {}".format(num1, num2, result)) 