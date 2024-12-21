def saving_users_data(username, password):
    # username must be in letters
    # password must be above 8 characters

    try:
        if not username.isalpha():
            raise Exception("--- Username must be in letters ---")
        
        if len(password) < 8:
            raise Exception("--- Password must be above 8 characters ---")
        
    except Exception as e:
        print(e)

    else:
        print("User Data Saved Successfully!")
        with open("users_info.txt", "w") as file:
            file.write(f"Username: {username}, Password: {password}\n")

    finally:
        print("Thank you for using our service")

saving_users_data("shreeporno", "123456789")