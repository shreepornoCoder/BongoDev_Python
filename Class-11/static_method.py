class User:
    company = "XYZ company"

    @staticmethod
    def get_company_name(): # Static Method
        return User.company
    
print(User.get_company_name())