from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update_temperature(self,new_temp):
        pass
    @abstractmethod
    def get_temperature(self):
        pass
class WeatherStation():
    def __init__(self,temperature) -> None:
        self.__temperature=temperature
        self.__observers=[]
    def get_temperature(self):
        print("The current temperature is:",self.__temperature)
    def  updated_temperature(self,new_temp):
        self.__temperature=new_temp
        print("The updated temperature is:",self.__temperature)
        self.notify()
    def notify(self):
        for x in self.__observers:
            x.update_temperature(self.__temperature)
    def add_observer(self,observer:Observer):
        self.__observers.append(observer)
    def remove_observer(self,observer:Observer):
        self.__observers.remove(observer)



class Mobile(Observer):
    def __init__(self):
        self.__temperature=0
    def update_temperature(self, new_temp):
        self.__temperature=new_temp
        print("the updated temprature for mobile is:",self.__temperature)
    def get_temperature(self):
        print("the current temperature for mobile is:",self.__temperature)

class Tv(Observer):
    def __init__(self):
        self.__temperature=0
    def update_temperature(self, new_temp):
        self.__temperature=new_temp
        print("the updated temprature for mobile is:",self.__temperature)
    def get_temperature(self):
            print("the current temperature for TV is:",self.__temperature)

weatherstation=WeatherStation(30)
mobile=Mobile()
tv=Tv()

weatherstation.add_observer(mobile)
weatherstation.add_observer(tv)

tv.get_temperature()
mobile.get_temperature()

weatherstation.updated_temperature(35)

tv.get_temperature()
mobile.get_temperature()

weatherstation.remove_observer(tv)
weatherstation.updated_temperature(50)
tv.get_temperature()
mobile.get_temperature()