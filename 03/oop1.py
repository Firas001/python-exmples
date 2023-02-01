

class Person:
    def __init__(self,Name,Age,ID):
        self.name=Name
        self.age=Age
        self.id=ID
        # print("OOP Lesson1")
    
    def getNamePrson(self):
        return self.name
    
    def getAgePerson(self):
        return self.age
    
    def getIdPerson(self):
        return self.id

obj = Person("Ali",25,91548722)
# print(dir(Person))
# print(dir(obj))
# print(obj.name,obj.id)
print(obj.getNamePrson())
obj2 = Person("Asma",20,2548622)
print(obj2.getNamePrson())