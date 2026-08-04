def product():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=a*b
    if c<=1000:
        return c
    else:
        return a+b
print(product())
