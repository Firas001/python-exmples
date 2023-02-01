

# Inheritance with hiding attribute (private data)
class A: #Super Class
    def __init__(self,name):
        self.__name=name
    
    def getName(self): #Accessor Method
        return self.__name
    
class B(A):# B is Child Class
    def __init__(self, name,age):
        super().__init__(name) # Call the constructor Method of super class
        self.age=age
    
    def getData(self):
        return f"The Name is: {self.getName()} and Age: {self.age}"
    
    def getInfo(self):
        return self.getName(),self.age


object=B("Ahmed",15)
print(object.getData())
print(f"Return Name from super class and Age from child class:\n\t\t{object.getInfo()}")