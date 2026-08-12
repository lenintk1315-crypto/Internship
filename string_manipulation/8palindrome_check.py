def palindrome(letter):
    letter=letter.lower()
    letter=letter.replace(""," ")
    if letter==letter[::-1]:
        return True
    else:
        return False


def main():
    letter=input("Enter the string :")
    result=palindrome(letter)
    print(result)
main()