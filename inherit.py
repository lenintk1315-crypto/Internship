class First():
    def __init__(self):
        print("This is first class")
    def display(self):
        print("This is display method of first class")
class Second(First):
    def __init__(self):
        print("This is second class")
    def display(self):
        print("This is display method of second class")
class Third(Second):# class Third(First,Second):  # Multiple inheritance
    def __init__(self):
        print("This is third class")
    def display1(self):
        print("This is display method of third class")
x=Third()
x.display1()
x.display()
print(Third.mro())    #Method Resolution Order