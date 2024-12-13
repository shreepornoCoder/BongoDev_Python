class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("")

class Lion(Animal):
    def make_sound(self):
        print("Roarrrrrrrrrrr")

lion = Lion("lion", 10)
lion.make_sound()