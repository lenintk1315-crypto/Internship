def product():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=a*b
    if c<=1000:
        return c
        print("The product is ", c)
    else:
        return a+b
        print("The sum is ", a+b)
print(product())