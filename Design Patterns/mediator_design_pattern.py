from typing import List
from abc import ABC, abstractmethod

class AirMediator(ABC):
    @abstractmethod
    def add_flight(self,flight):
        pass
    def send_message(self,message,from_flight):
        pass

class AirControl(AirMediator):
    def __init__(self) -> None:
        self.flights:List[Flight]=[]

    def add_flight(self, flight):
        self.flights.append(flight)

    def send_message(self, message, from_flight):
        for x in self.flights:
            if x.get_flight_no()!=from_flight: 
                x.recieve_message(message,x.get_flight_no())

class Flight():
    def __init__(self,flight_no,controller) -> None:
        self.__flight_no=flight_no
        self.controller:AirControl=controller
    def get_flight_no(self):
        return self.__flight_no

    def send_message(self,message):
        self.controller.send_message(message,self.get_flight_no())

    def recieve_message(self,message,flight_no):
        print(self.get_flight_no(),": message has been recieved from ",flight_no,message)

delhiController=AirControl()
spice=Flight("spice123",delhiController)
airIndia=Flight("air455",delhiController)
british=Flight("british1324",delhiController)
delhiController.add_flight(airIndia)
delhiController.add_flight(british)
delhiController.add_flight(spice)

spice.send_message("this is spice flight")
