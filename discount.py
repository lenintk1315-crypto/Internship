n=int(input("Enter the amount of purchased\n"))
if(n>5000):
    discount=n*0.1
    print("The discount amount is\n",discount)
else:
    print("No discount available\n")
totalamount=n-discount
print("The total amount",totalamount)
