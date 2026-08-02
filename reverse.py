def reverse(n):
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev
# print(reverse(int(input("Enter the number\n"))))
# print(reverse(1234))
n=int(input("Enter the number\n"))
print(reverse(n))
