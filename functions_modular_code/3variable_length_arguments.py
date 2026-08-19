def numeric_arguments(*args):
    total_sum=sum(args)
    count=len(args)
    return total_sum/count
def main():
    final_result=numeric_arguments(12,34,56,78,90)
    print(final_result)
main()
