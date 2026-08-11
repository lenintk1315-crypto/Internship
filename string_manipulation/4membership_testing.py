def vowel_checking(para):
    vowels=['a','e','i','o','u']
    count=0
    for i in para:
        if i in vowels:
            count+=1
    print(f"Total vowels : {count}")

def main():
    para=input("Enter the sentence :")
    print(para)
    vowel_checking(para)
main()