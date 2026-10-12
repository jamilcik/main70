class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name    # Attribute
        self.breed = breed  # Attribute

    # Behavior / Method
    def bark(self):
        return f"{self.name} says Woof!"


# Creating an object (instantiating the class)
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing attributes and calling methods
print(my_dog.name)    # Output: Buddy
print(my_dog.bark())  # Output: Buddy says Woof!

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"

# Child class inheriting from Animal
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"

cat = Cat("Whiskers")
print(cat.make_sound())  # Output: Whiskers says Meow!
