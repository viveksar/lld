from abc import ABC, abstractmethod 
class Order(ABC):
    @abstractmethod
    def execute(self):
        pass
class Chef():
    def make_burger(self):
        print("The chef is making burger")
    def make_pizza(self):
        print("the chef is making pizza")

class BurgerOrder(Order):
    def __init__(self,chef:Chef) -> None:
        self.__chef=chef
    def execute(self):
        print("the order for burger has been placed")
        self.__chef.make_burger()

class PizzaOrder(Order):
    def __init__(self,chef:Chef) -> None:
        self.__chef=chef
    def execute(self):
        print("pizza order")
        self.__chef.make_pizza()

class Waiter():
    def take_order(self,order:Order):
        order.execute()

w=Waiter()
c=Chef()
po=PizzaOrder(c)
bo=BurgerOrder(c)

w.take_order(po)
w.take_order(bo)