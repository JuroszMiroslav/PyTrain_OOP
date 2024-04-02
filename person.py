class Person:
    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age

    def showMsg(self):
        return(f'Jmenuji se {self.name} {self.surename} a je mi {self.age}')

clovek1 = Person("Pavel","Novak",45)
clovek1.showMsg()
#print(clovek1.spec)
class Student(Person):
    #spec = "devOps"
    def __init__(self, name, surename,age, spec):
        super().__init__(name, surename, age)
        self.spec = spec

    def showMsg(self):
        return (f'{super().showMsg()} a specializace je {self.spec}')



student1 = Student("Adam","Vesely",45,"HW")
print(student1.spec)
print(student1.showMsg())
print(clovek1.showMsg())