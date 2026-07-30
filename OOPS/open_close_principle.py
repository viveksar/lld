from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        print("parent payment method function")
        pass

class CreditCardPay(PaymentMethod):

    def pay(self,amount):
        print("amount paid from credit card",amount)

class UpiPay(PaymentMethod):
    def pay(self,amount):
        print("amount paid from upi pay",amount)

class PaypalPay(PaymentMethod):
    def pay(self,amount):
        print("amount paid from paypal",amount)

class ProcessPayment:
    def process_payment(self, payment_method:PaymentMethod,amount:int):
        print("payment process has started")
        payment_method.pay(amount)
        print("payment process has ended")

upi=UpiPay()
credit=CreditCardPay()
paypal=PaypalPay()
payment_process=ProcessPayment()
payment_process.process_payment(upi,44)
payment_process.process_payment(credit,777)
payment_process.process_payment(paypal,4432)