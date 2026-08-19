def multiple_return(list1):
        total_sum=sum(list1)
        count_avg=len(list1)
        return total_sum,total_sum/count_avg

def main():
    list1=list(map(int,(input("Enter the Values :")).split()))
    result=multiple_return(list1)
    print(result)
main()