def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius
    

def main():
    while True:
        choice=int(input("\n 1 celsius_to_fahrenheit \n 2 fahrenheit_to_celsius \n 3 Exit \n Enter the choice :"))
        if choice==1:
            c=float(input("Enter the celsius :"))
            print(f"fahrenheit : {celsius_to_fahrenheit(c)}")
        elif choice==2:
            f=float(input("Enter the fahrenheit :"))
            print(f"Celsius : {fahrenheit_to_celsius(f)}")
        else:
            print("Exiting...")
            break
main()