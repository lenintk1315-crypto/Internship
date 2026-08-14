def set_operation(list1,list2):
    list3=set()
    for i in list1:
        if i  in list2:
            list3.add(i)
    print(list3)

def main():
    list1=[1,2,3,4,5]
    list2=[4,5,6,7,8]
    set_operation(list1,list2)
main()