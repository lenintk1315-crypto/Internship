class student:
    year=2024
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def addage(self):
        self.age=self.age+1
    def display(self):
        print("name :",self.name)
        print("age :",str(self.age))
        print("rollno :",str(self.rollno))
    @classmethod
    def addyear(cls):
        cls.yaer=str(cls.year+1)
    @staticmethod
    def welcomed():
        print("Welcome to the class")
x=student("John",20,101)
y=student("Alice",22,102)
student.welcomed()
x.display()
y.display()
print("----------")
student.year=student.year+1
x.addage()
y.addage()

x.display()
y.display()

student.addyear()
print("----------")
x.addage()
y.addage()

x.display()
y.display()