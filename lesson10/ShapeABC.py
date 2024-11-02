from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, rrezja):
        self.rrezja = rrezja

    def area(self):
        return 3.14 * self.rrezja * self.rrezja

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

rrethi = Circle(3)
katrori = Square(10)
print(rrethi.area())
print(katrori.area())