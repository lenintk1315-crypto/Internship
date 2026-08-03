x=int(input("Enter the number: "))
if x<2:
    print("The number is less than 2")
    print("The no is still less than two")
print("Now ends")
for i in range(0,x):
    print(i)    
    if x>2:
        print("The number is greater than 2")
        print("done with iteration", i) 
print("Now ends")