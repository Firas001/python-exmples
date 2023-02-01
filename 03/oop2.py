

class Person:
    total=0
    def __init__(self):
        self.name=""
        self.age=0
        self.id=0
        Person.total +=1
    
    def getNamePrson(self):
        return self.name
    
    def getAgePerson(self):
        return self.age
    
    def getIdPerson(self):
        return self.id
    
    def setName(self):
        self.name= input("Enter Name:").strip()
    
    def setname2(self,N):
        self.name= N
    
    def setID(self):
        self.id= int(input("Enter ID:").strip())

    def getTotal(self):
        return f"you have {Person.total} object"


class B(Person):
    def __init__(self):
        super().__init__()
        self.collage="IT"
    
    def getCollg(self):
        return self.collage


# obj = Person()
# Nper=input("Enter Name:").strip()
# obj.setname2(Nper)
# print(obj.getNamePrson())
# obj2=Person()
# obj2.setName()
# obj2.setID()
# print(f"the name is {obj2.getNamePrson()} and ID: {obj2.getIdPerson()}")
# print(obj2.getTotal())
# obj3=Person()
# obj4=Person()
# print(obj3.getTotal())



h=B()
print(h.getNamePrson(),h.getCollg())