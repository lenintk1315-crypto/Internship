def anagram_check(name1,name2):
    if sorted(name1)==sorted(name2):
        return "Given string is Anagram"
    else:
        return "Given string is not Anagram"

def main():
    name1=input("Enter the first string :")
    name2=input("Enter the second string :")
    result=anagram_check(name1,name2)
    print(result)
main()