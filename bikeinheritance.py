class superbike:
    def __init__(self):
     print("This is a superbike class")
    def Ninja(self):
     price=int(200000)
     sound="Vroom Vroom"
     print("Price of Ninja is:",price)
     print(sound)
    def setname(self,name):
     self.name=name
     print("Name of the super bike is:",self.name)
class bike(superbike):
   def __init__(self):
        super().__init__()
        print("This is a bike class")
   def thunder(self):
     price=int(100000)
     self.sound="Broom Broom"
     print("Price of Thunder is:",price)
   def setname(self,name):
     super().setname(name)  
     self.name=name
     print("Name of the super bike is:",self.name)
    #  print(sound)
x=bike()
# y=superbike()
x.thunder()
print(x.sound)
x.Ninja()
x.setname("Thunder")
# x.setname("Ninja")
# y.setname("Ninja")



