from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def parameter(self):
        pass

class Circle(Shape):
    def __init__(self,r) -> None:
        super().__init__()
        self.radius=r
    def info(self):
        print("radius is ",self.radius)
    def area(self):
        print("area",self.radius*self.radius)
    def parameter(self):
        print("parameter")
c=Circle(10)
c.info()
c.parameter()
c.area()