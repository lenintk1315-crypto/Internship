def grade_check():
     grade=int(input("Enter the Mark:"))
     return grade
def main():
    grade=grade_check()
    if grade>90:
        print(f"{grade} - A Grade")
    elif grade>=80 and grade<=90:
        print(f"{grade} - B Grade")
    elif grade>=70 and grade<=80:
        print(f"{grade} C - Grade")
    elif grade>=60 and grade<=70:
        print(f"{grade} D - Grade")
    else: 
        print(f" F ")
main()
    