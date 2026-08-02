n1=int(input("Enter the account balance"))
n2=int(input("Enter the salary amount"))
bonus=n2+0.20
minbalace=30000
if bonus>50000:
    print("You are eligible for bonus")
else:
    print("You are not eligible for bonus")
Acbalance=n1+bonus
withdraw=int(input("Enter the amount to be withdraw"))
if(Acbalance-withdraw>=minbalace):
    print("Withdraw successfull")
else:
    print("You cant withdraw")