class Animal:

    species = ""

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def speak(self):
        raise NotImplementedError


class Dog(Animal):

    species = "mammal"

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def speak(self):
        print(f"{self.name} wof!")

    def __str__(self):
        return f"{self.name} wof!"


class Cat(Animal):

    species = "mammal"

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def speak(self):
        print(f"{self.name} meow!")

    def __str__(self):
        return f"{self.name} meow!"
