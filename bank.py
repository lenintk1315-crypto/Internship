balance=int(input("Enter the balance\n"))
def checkbalance(balance):
    print("The balance amount is ",balance)
def deposit(balance):
    amount=int(input("Enter the amount to be deposited\n"))
    balance+=amount
    print("The balance amount is ",balance)
    return balance
def withdraw(balance):
    amount=int(input("Enter the amount needed to be withdraw\n"))
    if amount<=balance+500:
        balance-=amount
        print("The balance amount is ",balance)
    else:
        print("Insufficient balance")
    return balance
while True:
    print("\n 1.check balance,\n 2. deposit,\n 3. withdraw,\n 4. Thankyou")
    choice=int(input("Enter your choice\n"))
    if choice==1:
        checkbalance(balance)
    elif choice==2:
        balance=deposit(balance)
    elif choice==3:
        balance=withdraw(balance)
    elif choice==4:
        print("Thankyou for using our services")
        break
    else:
        print("Invalid choice")
