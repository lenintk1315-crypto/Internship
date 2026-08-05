def login():
    password = input("Enter your password: ")
    if len(password)<8:
        print("Password is invalid : It should be at least 8 characters long")
    elif not any(char.isdigit() for char in password):
        print("Password is invalid : It should contain at least one digit") 
    elif not any(char.isupper() for char in password):
        print("Password is invalid : It should contain at least one uppercase letter")
    else:
        print("Password is valid")
login()