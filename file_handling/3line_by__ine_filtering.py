def file_filtering(count,keyword,file):
    for i in file:
        if keyword in i:
            count+=1
    return f"The Count of {keyword} in line is : {count} times"   


def main():
    with open("sample.txt","r") as file:
        count=0
        keyword=input("Enter the keyword to search :")
        result=file_filtering(count,keyword,file)
        print(result)
main()





















# def file_filtering():
#     with open("sample.txt","r") as file:
#         count=0
#         keyword=input("Enter the keyword to search :")
#         for i in file:
#             if keyword in i:
#                count+=1
#         print(f"The Count of {keyword} in line is : {count} times")
# file_filtering()