
print("start OOP in Python Language (: ")

class MyClass:

    def __init__(self,name,age):
        print("welcome inside Initialize Method")
        self.name=name
        self.age=age
    pass
    

# MyClass()
obj = MyClass("Ali",25)
obj2 = MyClass("Ahmed",30)
# print(dir(MyClass))
# print(dir(str))
print(obj.name,obj.age)
print(obj2.name,obj2.age)


# print(dir(obj))
# print(obj.__class__)