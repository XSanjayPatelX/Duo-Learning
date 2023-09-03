# A constructor is a function that gets called at the time of creating an object. LINE 10, want to pass x or y values
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)

# Exercise
# Define a new type called person
# Person object should have name object and a talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
john.talk()

# Exercise 2
class Personn:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Personn("John Smith")
john.talk()

bob = Personn("Bob Smith")
bob.talk()