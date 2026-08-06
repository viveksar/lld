from abc import ABC, abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass
    @abstractmethod
    def direction(self):
        pass

class Transportation():
    def __init__(self,mode:TransportMode) -> None:
        self.transport_mode:TransportMode=mode

    def change_mode(self,mode:TransportMode):
        self.transport_mode=mode

    def get_mode(self):
        return self.transport_mode

    def eta(self):
        return self.transport_mode.eta()

    def direction(self):
        return self.transport_mode.direction()

class Bike(TransportMode):
    def eta(self):
        print("The eta for bike is 10 mins")
    def direction(self):
        print("The direction is go left then right then straight")

class Walk(TransportMode):
    def eta(self):
        print("eta of waliking is 55 mins")
    def direction(self):
        print("the direction is left,right,left,left straight")

bike=Bike()
walk=Walk()
transportation=Transportation(bike)
transportation.eta()
transportation.direction()
transportation.change_mode(walk)
transportation.eta()
transportation.direction()