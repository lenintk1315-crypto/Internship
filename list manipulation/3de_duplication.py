def duplicate(list1,list2):
    for i in list1:
            if i not in list2:
                list2.append(i)
    print(list2)

def main():
    list1=[1,2,3,1,3,3,4,4,4,5]
    list2=[]
    duplicate(list1,list2)
main()