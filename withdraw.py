n=int(input("Enter the balance"))
n1=int(input("Enter the amount to be withdraw"))
minbalance=500
if(n-n1>=minbalance):
    print("Withdraw successfull:")
else:
    print("You cant withdraw the amount because your balance is less than minimum balance   of 500")
currentbalance=n-n1
print(currentbalance)
