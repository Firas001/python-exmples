
# Hiding Attribute : the name of attribute must be start with (__) two underscore
# 
# Hiding Attributes: slide 14 in ppt file.
# Accessor and Mutator Methods slide 17 in ppt file. 

class Person:
    total=0
    def __init__(self):
        self.__name=""
        self.__age=0
        self.__id=0
        Person.total +=1
    # Accessor Method: return value from class’s attribute without changing it
    def getNamePrson(self):
        return self.__name
    
    def getAgePerson(self):
        return self.__age
    
    def getIdPerson(self):
        return self.__id
    
    # Mutator methods: store or change the value of a data attribute
    def setName(self):
        self.__name= input("Enter Name:").strip()
    
    def setName2(self,N):
        self.__name= N
    
    def setID(self):
        self.__id= int(input("Enter ID:").strip())

    def getTotal(self):
        return f"you have {Person.total} object"



obj1=Person()
obj2=Person()
obj3=Person()

obj1.setName2("Ahmed")
obj2.setName2("Ali")
obj3.setName2("Fatma")
print(obj1.getNamePrson())
print(obj2.getNamePrson())
print(obj3.getNamePrson())
print(f"the Number Of Objects is:\n\t\t {Person.getTotal(obj1)}") # passing object as Argument
print(f"the Number Of Objects is:\n\t\t {obj2.getTotal()}")




