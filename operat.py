class First():
    def setname(self,name):
        self.name=name
        print(" Enter The First name",self.name)
class Second(First):
    def setname(self,name):
        self.name=name
        print(" Enter The Second name",self.name)
    def __add__(self,other):
        name=self.name+" "+other.name
        return name
firstname=Second()
secondname=Second()
firstname.setname("John")
secondname.setname("Alice")
fullname=firstname+secondname
print("Full name is:",fullname)
