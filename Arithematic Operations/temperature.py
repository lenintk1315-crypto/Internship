def temp():
    set=int(input("Enter the choice:\n1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit\n..Enter the choice:"))
    if set==1:
        f=float(input("Enter temperature in Fahrenheit: "))
        c=(f-32)*5/9
        print("The tempertaure in celsius:",c)
    elif set==2:
        c=float(input("Enter the temperature in clecius:"))
        f=(c*9/5)+32
        print("The temperature in fahrenheit:",f)
    else:
        print("No Answer")
    
print(temp())