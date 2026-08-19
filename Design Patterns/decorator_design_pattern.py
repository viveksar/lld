from abc import abstractmethod, ABC

class Bevrage(ABC):
    @abstractmethod
    def get_description(self):
        pass
    def get_price(self):
        pass
class Coffee(Bevrage):
    def get_description(self):
        print("coffee descriiptin")
        return "coffee description"
    def get_price(self):
        return 20

class AddonDecorator(Bevrage):
    def __init__(self,coffee:Coffee) -> None:
        self.coffee=coffee
    def get_price(self):
        pass
    def get_description(self):
        pass

class Creamcoffee(AddonDecorator):
    def get_price(self):
        return self.coffee.get_price()+10
    def get_description(self):
        return self.coffee.get_description()+" cream coffee"
class MilkCoffee(AddonDecorator):
    def get_price(self):
        return self.coffee.get_price()+40
    def get_description(self):
        return self.coffee.get_description()+" milk in this coffee"

coffee=Coffee()
print(coffee.get_description())
print(coffee.get_price())
creamcoffee=Creamcoffee(coffee)

print(creamcoffee.get_description())
print(creamcoffee.get_price())

milkcoffee=MilkCoffee(coffee)

print(milkcoffee.get_description())
print(milkcoffee.get_price())