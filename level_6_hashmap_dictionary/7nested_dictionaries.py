def nested_dictionary(student,name):
    print("Report card :")
    print("student :",name)
    for sub,grade in student[name].items():
        print(f"{sub} : {grade} ")


def main():
    student = {
    "antony": {
        "Python": 90,
        "Reasoning" : 70,
        "GK"   : 78
}
    }
    name=input("Enter the student name :")
    nested_dictionary(student,name)
main()