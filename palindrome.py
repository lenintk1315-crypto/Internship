def palindrome(name):
    # return print(name==name[::-1])
    if name==name[::-1]:
        return True
    else:
        return False
# print(palindrome(input("Enter the string\n")))
name=input("Enter the string\n")
print(palindrome(name))
