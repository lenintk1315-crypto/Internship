def boundary_comparison(list1):
        if list1[0]==list1[-1]:
            return True
        else:
            return False
def main():
    list1=[10,20,30,40,10]
    result=boundary_comparison(list1)
    print(result)
main()