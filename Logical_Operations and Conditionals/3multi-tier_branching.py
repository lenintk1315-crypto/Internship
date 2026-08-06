def branching():
    amount = float(input("Enter an amount: "))
    if amount<=10000:
        print("No tax is applicable")
    elif amount>10000 and amount<=20000:
        tax=(amount-10000)*0.1
        print(f"The tax is :{tax}")
    elif amount>20000:
        tax=(amount-20000)*0.2 + (10000*0.1)
        print(f"The tax is :{tax}")
branching()
