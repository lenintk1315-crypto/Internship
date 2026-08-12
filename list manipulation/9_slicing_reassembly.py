def rotating_slicing(list,n):
    result=list[n:]
    result.extend(list[:n])                                           # result=list[n:] + list[:n]
    print(result)

def main():
    list=[1,2,3,4,5]
    n=int(input("Enter the no :"))
    rotating_slicing(list,n)
main()