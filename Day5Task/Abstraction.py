from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_Sound(self):
        pass

class Lion(Animal):
    def make_Sound(self):
        print("Roar!")

class Dog(Animal):
    def make_Sound(self):
        print("woof!")

lion = Lion()
lion.make_Sound()
dog = Dog()
dog.make_Sound()