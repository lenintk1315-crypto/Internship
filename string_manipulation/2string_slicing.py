def remove_chars(s,name):
        print(name[s:])

def main():
    name=input("Enter the character :")
    s=int(input("Enter the Number :"))
    remove_chars(s,name)
    print(f"{name}")
main()