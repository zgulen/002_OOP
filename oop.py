from cgi import test
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))

# test = [122,"victor", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:X]
# print_types(test)

# class Person:
#     name = "Zübeyir"
#     age = 31

# person1 = Person()
# person2 = Person()
# print(person1.name)
# Person.job = "Developer"
# print(person1.job)


# class Person:
#     company = "clarusway"
#     def test(self):
#         print("test")
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
#     def get_details(self):
#         print(self.name, self.age)

#     @staticmethod
#     def salute():
#         return "hi there"

# person1 = Person()
# person2 = Person()

# person1.location = "Turkey"
# person2.age = 18
# print(person1.location)
# print(person2.age)
# print(person1.age)

# person1.test()
# person1.set_details("zübeyir", 31)
# person1.get_details()
# print(person1.salute())

#! special methods (init, str)

# class Person():
#     company = "Google"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     def __str__(self):
#         return f"{self.name} - {self.age}"


# person1 = Person("zübeyir", 31)
# person1.get_details()
# print(person1)


# ! ENCAPSULATİON
class Person:
    company = "clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = 5000
        self.__id = 3000

    def __str__(self):
        return f"{self.name} - {self.age}"

    def get_details(self):
        print(self.name, self.age)

# person1 = Person("zübeyir", 31)
# person1._id = 3535
# person1._Person__id = 3235
# print(person1._id)
# print(person1._Person__id)


#! Abstraction
liste = [4, 3, 2, 1, 5]
liste.sort()
print(liste)

#! inheritance an polymorphism


class Employee(Person):
    def __init__(self, name, age, path):
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.path = path
    
    def get_details(self):
        print(self.name, self.age, self.path)

emp1 = Employee("zübeyir", 31, "FS")
emp1.get_details()
print(emp1)

















print("-----------------------------------")
