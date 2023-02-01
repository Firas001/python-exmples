
class MyClass:
    total=0
    def __init__(self):
        self.name=""
        self.age=0
        MyClass.total+=1
    
    def setName(self):
        self.name=input("Enter name:").strip().capitalize()
    
    def setAge(self):
        self.age=int(input("Enter age:").strip())
    def getTotal(self):
        return MyClass.total

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getInfo(self):
        return f"the Name is {self.name} and Age is: {self.age}"

class B(MyClass):
    def __init__(self):
        super().__init__()

# print(dir(MyClass))
# name=input("Enter name").strip()
# object1=MyClass(name,22)
# print(object1.getName(),object1.getAge())
# object1=MyClass()
# object1.setName()
# object1.setAge()
# print(object1.getInfo())
# print(MyClass.getInfo(object1))
# print(f"Now you have {MyClass.getTotal(object1)} object")
# print(f"Now you have {object1.getTotal()} object")
# object2=MyClass()
# object2.setName()
# print(object2.getInfo())
# print(f"Now you have {object1.getTotal()} object")
# object3=MyClass()
# object4=MyClass()
# objectf=MyClass()
# print(f"Now you have {objectf.getTotal()} object")

object1=B()
object1.setAge()
print(object1.getAge())
