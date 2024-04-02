







import random
class Student:

    spec = "devOps"
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.__personID=random.randint(1,100)

    def showMsg(self):
        print(f'moje jmeno je {self.name} a muj vek je {self.age} a ID je {self.__getID()}')

    def __getID(self):
        return f'{self.__personID}'
    def sayHi(self, pozdrav):
        print(f'{pozdrav}, moje jmeno je {self.name}')

    def checkAlcohol(self):
        if self.age>18:
            rozhodnut = "pije"
        else:
            rozhodnut = "nepije"
        print(rozhodnut)
student = Student("Adam",55)
student.showMsg()


#print(student.age)
# student.checkAlcohol()
# #student.__age = 15
# student.checkAlcohol()


# student1 = Student("Osel",55)
# student.showMsg()
# student.checkAlcohol()
# student.age = 16
# student.checkAlcohol()
#
#student.sayHi("ahoj")#ahoj, ja jsem Adam
# student.sayHi("Dobry den") #Dobry den, ja jsem Osel
#
#
# def pozdrav(volani):
#     print(f"{volani} ja jsem karel")
#
# pozdrav("Dobry")

# student1=Student("Pavel",2000)
# print(student1.age)
# #
# student2 = Student("Adam",1999)
# print(student2.age)
# print(student2.spec)
# student2.name = "Petr"
# print(student2.name)