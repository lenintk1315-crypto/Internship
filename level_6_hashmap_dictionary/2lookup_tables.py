def dictionary_creation(dict1):
    for i in range(1,11):
        dict1[i]=i**2
    print(dict1)


def main():
    dict1={}
    dictionary_creation(dict1)
main()