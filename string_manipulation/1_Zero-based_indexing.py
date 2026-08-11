def zero_indexing(value):
    for index,value in enumerate(value):
        if index%2==0:
            print(index,value)

def main():
    value=input("Enter the character :")
    zero_indexing(value)
    print(value)
main()