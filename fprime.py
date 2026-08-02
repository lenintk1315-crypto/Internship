def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False

    return True
num=int(input("Enter the number\n"))
if isprime(num):
     print("The number is prime")
else:
    print("Not prime")
    