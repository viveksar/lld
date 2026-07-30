from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self,amount):
        pass
class FirstOrder(DiscountStrategy):
    def calculate_discount(self,amount):
        print("The discount for this is 100 rs on first order. Discount:",100, "Amount to pay:",max(0,amount-100))

class Tenpercent(DiscountStrategy):
    def calculate_discount(self,amount):
        print("The discount as per this strategy is 10% of total amount","Discount:",.1*amount,"Amount to pay:",.9*amount)

class DiscountService():
    def __init__(self,discount_strategy:DiscountStrategy) -> None:
        self.__active_strategy=discount_strategy
        self.amount=0

    def update_amount(self,amount):
        self.amount=amount

    def calculate_discount(self):
        self.__active_strategy.calculate_discount(self.amount)

    def change_discount(self,new_strategy):
        self.__active_strategy=new_strategy

fo=FirstOrder()
tp=Tenpercent()

discount=DiscountService(fo)
discount.update_amount(1000)
discount.calculate_discount()
discount.change_discount(tp)
discount.calculate_discount()