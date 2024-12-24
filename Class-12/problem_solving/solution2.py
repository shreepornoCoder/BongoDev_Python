import random
import string

class Bank:
    bank_name = "Developers Banking System Limited"
    def __init__(self, id, username, password, balance):
        self.id = id
        self.username = username
        self.__password = password
        self.balance = balance

    def deposit_money(self, money_amount):
        self.balance += money_amount

        return self.balance

    def withdraw_money(self, money_amount):
        self.balance -= money_amount

        return self.balance

    def check_balance(self):
        return self.balance

# account creation
id = random.randint(1000, 9999)
special_symbols = list(string.punctuation)
run = True
isbanking = False

while run:
    try:
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        balance = input("Enter Your Welcome Balance: ")
        # print(list(password) not in special_symbols)

        if len(password) < 8 and (list(password) not in special_symbols):
            raise Exception("Password must be at least 8 characters and contain special symbols (#, @, $, & etc)!")
        
        elif int(balance) < 0:
            raise Exception("Balance must be greater than 0!")
        
        elif not balance.isdigit():
            raise Exception("Invalid Amount!")
        
        elif not username[0].isalpha():
            raise Exception("Username must start with a letter!")
        
    except Exception as e:
        print(e)

    else:
        global user1

        balance = int(balance)
        user1 = Bank(id, username, password, balance)
        print("Account Created Successfully!")
        print("Welcome {} to {}".format(user1.username, Bank.bank_name))
        run = False 
        isbanking = True

# banking operations
run = True
if isbanking:
    print("----------------------------------------")
    while run:
        print("1. Check Balance")   
        print("2. Deposit Money")   
        print("3. Withdraw Money")   
        print("4. Exit")

        operation = int(input("Enter Your Operation: "))

        if operation == 1:
            print("Your Current Balance is: {}".format(user1.check_balance()))

        # Deposit Money
        elif operation == 2:
            run_ope = True
            while run_ope:
                try:
                    money_amount = input("Enter Deposit Money Amount: ")
                    if not money_amount.isdigit() or int(money_amount) < 0:
                        raise Exception("Invalid Money Amount!") 
                    
                except Exception as e:
                    print(e)

                else:
                    money_amount = int(money_amount)
                    user1.deposit_money(money_amount)

                    print("Money Deposited Successfully!")
                    print("Your Current Balance is: {}".format(user1.balance))
                    run_ope = False

        # Withdraw Money
        elif operation == 3:
            run_ope = True
            while run_ope:
                try:
                    money_amount = input("Enter Withdraw Money Amount: ")
                    if not money_amount.isdigit() or int(money_amount) < 0 or int(money_amount) == 0:
                        raise Exception("Invalid Money Amount!") 
                    
                except Exception as e:
                    print(e)

                else:
                    money_amount = int(money_amount)
                    user1.withdraw_money(money_amount)

                    print("Money Withdraw Successfully!")
                    print("Your Current Balance is: {}".format(user1.balance))
                    run_ope = False
        
        elif operation == 4:
            run = False
            print("Thank you for using our program!")

        else:
            print("You selected Invalid Operation!") 

