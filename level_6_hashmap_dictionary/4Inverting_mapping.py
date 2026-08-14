def inverting_dictionary(dict1):
    result={}
    for i,j in dict1.items():
        result[j]=i
    return result

def main():
    dict1={
         "a":1,"b":2,"c":5
    }
    final_result=inverting_dictionary(dict1)
    print(final_result)
main()






