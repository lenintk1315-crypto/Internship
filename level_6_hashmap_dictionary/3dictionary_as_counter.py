def dictionary_counter(dict1):
    count={}
    for i in dict1.split():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count)


def main():
    dict1=input("Enter the sentence :")
    dictionary_counter(dict1)
main()