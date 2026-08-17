def calculator_sum(num1,num2):
    return num1+num2
def mult_calculator(num1,num2):
    return num1*num2
def div_calculator(num1,num2):
    return num1/num2
def sub_calculator(num1,num2):
    return num1-num2
    

def calculator_main():
    while True:
        choice=int(input(" 1.Sum  \n 2.Multiplication  \n 3.Division  \n 4.substraction \n 5.Exit \n Enter the choice :"))
        match choice:
            case 1:
                num1=int(input("Enter the 1st Number :"))
                num2=int(input("Enter the 2nd Number :"))
                print(f"The sum of {num1} and {num2} is {calculator_sum(num1,num2)}")
            case 2:
                num1=int(input("Enter the 1st Number :"))
                num2=int(input("Enter the 2nd Number :"))
                print(f"The Multiplication of {num1} and {num2} is {mult_calculator(num1,num2)}")
            case 3:
                num1=int(input("Enter the 1st Number :"))
                num2=int(input("Enter the 2nd Number :"))
                print(f"The Div of {num1} and {num2} is {div_calculator(num1,num2)}")
            case 4:
                num1=int(input("Enter the 1st Number :"))
                num2=int(input("Enter the 2nd Number :"))
                print(f"The Sub of {num1} and {num2} is {sub_calculator(num1,num2)}")
            case 5:
                print("Exited ...Thank You......")
                break
            case _:
                print("Invalid choice..please enter the Number from 1 to 5..")

calculator_main()