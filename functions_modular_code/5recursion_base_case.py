def factorial_check(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_check(n-1)
n=int(input("Enter the limit :"))
result=factorial_check(n)
print(result)