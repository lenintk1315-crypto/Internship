def merge_dictionary(dict1,dict2):
    dict1.update(dict2)
    print(dict1)


def main():
    dict1={"name":"Alice","age":25}
    dict2={"city":"NY","job":"Engineer"}
    merge_dictionary(dict1,dict2)
main()