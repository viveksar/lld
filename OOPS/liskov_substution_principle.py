from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,balance) -> None:
        self.balance=balance
    @abstractmethod
    def deposit(self,amount):
        pass

class Withdraw(Account):
    def __init__(self, balance) -> None:
        super().__init__(balance)

    @abstractmethod
    def withdraw(self,amount):
        pass

class SavingAccount(Withdraw):
    def __init__(self, balance) -> None:
        super().__init__(balance)
    def deposit(self, amount):
        self.balance+=amount
        print("Amount deposited",amount,"Total Balance:",self.balance)
    def withdraw(self, amount):
        if(amount>self.balance):
            print("cannot withdraw")
        else:
            self.balance-=amount
            print("amount withdrawn, Total Balance remaning",self.balance)

class FixedAccount(Account):
    def __init__(self, balance) -> None:
        super().__init__(balance)

    def deposit(self, amount):
        self.balance+=amount
        print("amount deposited. total balance:",self.balance)

saving=SavingAccount(100)
saving.deposit(88)
saving.withdraw(798)
saving.withdraw(78)


fixed=FixedAccount(88)
fixed.deposit(77)
fixed.deposit(56)