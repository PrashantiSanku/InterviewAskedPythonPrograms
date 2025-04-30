'''
Functional code challenge: A dog can bark!
Your task:
Create a Python class named Dog.
Define two attributes within the Dog class: name (a string to store the dog's name) and
breed (a string to store the dog's breed).
Implement a method named bark() within the Dog class. This method should print a message
to the console that includes the dog's name and breed, something like: "Woof! My name is
[name] and I'm a [breed]."
Create an instance (object) of the Dog class, name it my_dog,
Using the my_dog variable instance. call the bark() method, providing the name Buddy and
the breed Golden Retriever to see it in action!

Tips:
Remember to use the __init__ method to initialize the name and breed attributes when creating a new Dog object.
Within the bark() method, use self.name and self.breed to access the dog's attributes.

Example input:
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()

Expected output:
Woof! My name is Buddy and I'm a Golden Retriever.
'''

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}")
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()