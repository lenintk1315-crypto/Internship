def bucket_sorting(list1,even,odd):
    for i in list1:
        if i%2==0:
            even.append(i)
        elif i%2!=0:
            odd.append(i)
    print(f" Even list :{even}\n Odd list :{odd}")
def main():
    list1=[12,7,34,21,5,10,8,3,19,2]
    even=[]
    odd=[]
    bucket_sorting(list1,even,odd)
main()