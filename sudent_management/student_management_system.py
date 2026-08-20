def add_student(student,add_stud):
    student[add_stud]={}
    return student
    

def add_marks(student,stud_mark,add_stud,subject):
    student[add_stud][subject]=stud_mark
    return student
    

def search_student(search,student):
    if search in student:
        return f"Student Found{search}"
    else:
        return (f"{search} Student Not Found : ")
    

def highest_mark(student,add_stud):
    highest=0
    highest_sub=" "
    for key,mark in student[add_stud].items():
        if mark > highest:
            highest=mark
            highest_sub=key
    return f"The highest mark is :{highest_sub} :{highest} "
    

def view_student(student, add_stud):
    for subject, mark in student[add_stud].items():
        return(f"Subject: {subject}, Mark: {mark}")

def calculate_avg(student,add_student):
    count=0
    total_sum=0
    for key,mark in student[add_student].items():
        total_sum+=mark
        count+=1
    try:
        
        average=total_sum/count
        return average
    except ZeroDivisionError:
            return ("Zero division error")


def main_student():
    student={}
    while True:
        choice=int(input(" \n 1. Add the student \n 2. Add Marks \n 3. search student \n 4. Highest Mark \n 5. view student \n 6. Average Mark \n 7. Exit \n Enter the choice :"))
        match choice:
            case 1:
                add_stud=input("Enter The Student To add :")
                print(f"students : {add_student(student,add_stud)}")
            case 2:
                add_stud = input("Enter the student: ")

                if add_stud in student:
                    subject = input("Enter the subject: ")
                    stud_mark = int(input("Enter the student mark: "))

                    print(add_marks(student, stud_mark, add_stud, subject))
                else:
                    print("Student not found. Add the student first.")
            case 3:
                search=input("Enter the student to search :")
                print(f"Search Student : {search_student(search,student)}")
            case 4:
                add_stud = input("Enter the student: ")

                if add_stud in student:
                    print(f"Highest Mark: {highest_mark(student, add_stud)}")
                else:
                    print("Student not found")
            case 5:
                add_stud = input("Enter the student: ")

                if add_stud in student:
                    print(view_student(student, add_stud))
                else:
                    print("Student not found")

            case 6:

                add_stud = input("Enter the student: ")

                if add_stud in student:
                    print(f"Average: {calculate_avg(student, add_stud)}")
                else:
                    print("Student not found")
            case 7:
                print("Exiting.....")
                break
main_student()