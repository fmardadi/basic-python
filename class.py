class MyClass:
    x = 5

p1 = MyClass()
p2 = MyClass()
# print(p1.x)
# print(p2.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("Hello my name is " + self.name)
    
person1 = Person("Farhan", 21)
person2 = Person("Andi", 18)
print(person1.name)
print(person2.name)

person1.greeting()
person2.greeting()