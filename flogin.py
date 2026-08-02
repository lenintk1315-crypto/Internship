def credentials(username ,password):
    savedusername="lenin"
    savedpassword="lenintk@2002"
    if username==savedusername and password==savedpassword:
        return "successfull"
    else:
        return "unsuccessfull"
username=input("Enter the username\n")
password=input("Enter the password\n")
print(credentials(username,password))