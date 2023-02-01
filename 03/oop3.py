
# Inheritance 
class A: #Super Class
    def __init__(self,name):
        self.name=name
    
    def getName(self): #Accessor Method
        return self.name
    
class B(A):# B is Child Class
    def __init__(self, name,age):
        super().__init__(name) # Call the constructor Method of super class
        self.age=age
    
    def getData(self):
        return f"The Name is: {self.name} and Age: {self.age}"
    
    def getInfo(self):
        return self.getName(),self.age


object=B("Ahmed",15)
print(object.getData())
print(f"Return Name from super class and Age from child class:\n\t\t{object.getInfo()}")